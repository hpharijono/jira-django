import pytest

from project.factories.project_factory import ProjectFactory
from ticket.factories.ticket_factory import TicketFactory
from ticket.models import Ticket


@pytest.mark.django_db
class TestTicketViews:
    def test_create_ticket(self, client):
        project = ProjectFactory()
        assert Ticket.objects.count() == 0
        response = client.post("/tickets/", {"title": "Ticket1", "project": project.id})
        assert response.status_code == 201
        assert Ticket.objects.count() == 1

    def test_list_tickets(self, client):
        TicketFactory.create_batch(5)
        response = client.get("/tickets/")
        assert response.status_code == 200
        assert Ticket.objects.count() == 5

    def test_get_ticket(self, client):
        ticket = TicketFactory(title="Ticket1", description="Test Description")
        response = client.get(f"/tickets/{ticket.id}/")
        assert response.status_code == 200
        assert response.json() == {
            "assignee": None,
            "description": "Test Description",
            "created_at": ticket.created_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
            "id": ticket.id,
            "title": "Ticket1",
            "project": ticket.project.id,
            "status": "To Do",
            "updated_at": ticket.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
        }

    def test_update_ticket(self, client):
        ticket = TicketFactory()
        response = client.put(
            f"/tickets/{ticket.id}/",
            {"title": "KitKat", "status": "In Progress", "project": ticket.project.id},
            content_type="application/json",
        )
        assert response.status_code == 200
        ticket.refresh_from_db()

        assert ticket.title == "KitKat"
        assert ticket.status == "In Progress"

    def test_delete_ticket(self, client):
        ticket = TicketFactory()
        assert Ticket.objects.count() == 1
        response = client.delete(f"/tickets/{ticket.id}/")
        assert response.status_code == 204
        assert Ticket.objects.count() == 0

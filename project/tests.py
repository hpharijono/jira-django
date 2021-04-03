import pytest

from project.factories.project_factory import ProjectFactory
from project.models import Project
from ticket.factories.ticket_factory import TicketFactory


@pytest.mark.django_db
class TestProjectViews:
    def test_create_project(self, client):
        assert Project.objects.count() == 0
        response = client.post("/projects/", {"name": "KitKat", "code": "KTKT"})
        assert response.status_code == 201
        assert Project.objects.count() == 1

    def test_list_projects(self, client):
        ProjectFactory.create_batch(5)
        response = client.get("/projects/")
        assert response.status_code == 200
        assert Project.objects.count() == 5

    def test_get_project(self, client):
        project = ProjectFactory(name="Project1", code="P1")
        response = client.get(f"/projects/{project.id}/")
        assert response.status_code == 200
        assert response.json() == {
            "code": "P1",
            "created_at": project.created_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
            "id": project.id,
            "name": "Project1",
            "updated_at": project.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
        }

    def test_update_project(self, client):
        project = ProjectFactory()
        response = client.put(
            f"/projects/{project.id}/",
            {"name": "KitKat", "code": "KTKT"},
            content_type="application/json",
        )
        assert response.status_code == 200
        project.refresh_from_db()

        assert project.name == "KitKat"
        assert project.code == "KTKT"

    def test_delete_project(self, client):
        project = ProjectFactory()
        assert Project.objects.count() == 1
        response = client.delete(f"/projects/{project.id}/")
        assert response.status_code == 204
        assert Project.objects.count() == 0

    def test_project_tickets(self, client):
        project = ProjectFactory()
        TicketFactory.create_batch(3, project=project)
        response = client.get(f"/projects/{project.id}/tickets/")
        assert response.status_code == 200
        assert len(response.json()) == 3

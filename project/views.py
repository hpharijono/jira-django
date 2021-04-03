from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from project.models import Project
from project.serializers import ProjectSerializer
from ticket.models import Ticket
from ticket.serializers import TicketSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    @action(detail=True, methods=["get"], url_path="tickets")
    def tickets(self, request, pk):
        tickets = Ticket.objects.filter(project_id=pk)
        data = TicketSerializer(tickets, many=True).data
        return Response(data)

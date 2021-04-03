from rest_framework import viewsets

from ticket.models import Ticket
from ticket.serializers import TicketSerializer


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

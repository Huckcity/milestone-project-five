from rest_framework import viewsets, permissions
from tickets.models import Ticket

from .serializers import TicketSerializer


class TicketViewSet(viewsets.ModelViewSet):

    queryset = Ticket.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TicketSerializer

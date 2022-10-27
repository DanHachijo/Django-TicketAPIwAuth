# from msilib.schema import ServiceInstall
from tickets.models import Ticket, TicketCategory
from .serializers import TicketSerializer, TicketReadSerializer,CategorySerializer
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = TicketCategory.objects.all()
    serializer_class = CategorySerializer

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all().order_by('-ticket_date')
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['store__id', 'is_open']

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return TicketReadSerializer
        return TicketSerializer
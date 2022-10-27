from django.contrib import admin
from .models import TicketCategory, Ticket

tickets = [TicketCategory, Ticket]
admin.site.register(tickets)


# from cgitb import lookup
from rest_framework import serializers
from .models import Ticket, TicketCategory
from members.models import Member

from members.serializers import MemberSerializer
from customers.serializers import CustomerContactReadSerializer, StoreSerializer, CompanySerializer


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = TicketCategory
        fields = "__all__"
        # fields = ["id", "name"]


class TicketSerializer(serializers.ModelSerializer):
    # ticket_date = serializers.DateTimeField()
    ticket_date = serializers.DateTimeField(
        format="%m/%d/%Y %H:%M", input_formats=["%m/%d/%Y %H:%M"])

    # complete_by = serializers.DateField(allow_null=True)
    # complete_by = serializers.DateField(
    #     format="%m/%d/%Y", allow_null=True)
    complete_by = serializers.DateField(
        format="%m/%d/%Y", input_formats=["%m/%d/%Y"], allow_null=True)
    class Meta:
        model = Ticket
        fields = '__all__'
        # depth = 1

class TicketReadSerializer(TicketSerializer):
    category = CategorySerializer(read_only=True)
    updated_by = MemberSerializer(read_only=True)
    created_by = MemberSerializer(read_only=True)
    escalated_to = MemberSerializer(read_only=True)
    contact = CustomerContactReadSerializer(read_only=True)
    store = StoreSerializer(read_only=True)
    company = CompanySerializer(read_only=True)
    # date = serializers.DateTimeField(
    #     format="%m/%d/%Y %H:%M", input_formats=["%m/%d/%Y %H:%M"])

from rest_framework import serializers
from .models import Member, Office

class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = "__all__"


class MemberSerializer(serializers.ModelSerializer):
    office = OfficeSerializer()

    class Meta:
        model = Member
        fields = ["id", "user_name", "email", "first_name",
                  "last_name", "phone", "title", "office"]

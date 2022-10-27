from rest_framework import serializers
from .models import Store, Company, CustomerContact
# from .serializer import CompanySerializer
# class StoreSerializer(serializers.Serializer):


# class CompanyListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Company
#         fields = ['id', 'name', 'state']


class CompanySerializer(serializers.ModelSerializer):
    date = serializers.DateField(
        format="%m/%d/%Y", read_only=True)

    class Meta:
        model = Company
        fields = '__all__'

# class CompanyReadSerializer(CompanySerializer):

#     class Meta:
#         model = Company
#         fields = '__all__'


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'


# class StoreListSerializer(serializers.ModelSerializer):
#     company = CompanyListSerializer(read_only=True)

#     class Meta:
#         model = Store
#         fields = ['id', 'name', 'state', 'company' ]


class StoreReadSerializer(StoreSerializer):
    date = serializers.DateField(
        format="%m/%d/%Y", read_only=True)
    company = CompanySerializer(read_only=True)


class CustomerContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerContact
        fields = '__all__'


class CustomerContactReadSerializer(CustomerContactSerializer):
    store = StoreSerializer()
    company = CompanySerializer()

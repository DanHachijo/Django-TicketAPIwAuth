from .models import Store, Company, CustomerContact
from .serializers import (
    CompanySerializer,
    # CompanyListSerializer,
    StoreSerializer,
    # StoreListSerializer,
    StoreReadSerializer,
    CustomerContactSerializer,
    CustomerContactReadSerializer,
    )
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


# from rest_framework_serializer_extensions.views import SerializerExtensionsAPIViewMixin


class CompanyViewSet(viewsets.ModelViewSet):
    # queryset = Company.objects.filter(is_customer=True)
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['store__id']

# class CompanyListViewSet(viewsets.ModelViewSet):
#     queryset = Company.objects.all()
#     serializer_class = CompanyListSerializer

class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return StoreReadSerializer
        return StoreSerializer

# class StoreListViewSet(viewsets.ModelViewSet):
#     queryset = Store.objects.all()
#     serializer_class = StoreListSerializer

class CustomerContactViewSet(viewsets.ModelViewSet):
    queryset = CustomerContact.objects.all()
    serializer_class = CustomerContactSerializer
    filter_backends = [DjangoFilterBackend]
    # search_fields = ['store__id', 'company__id']
    filterset_fields = ['store__id', 'company__id']


    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return CustomerContactReadSerializer
        return CustomerContactSerializer
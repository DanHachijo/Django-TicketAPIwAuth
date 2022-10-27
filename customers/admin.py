from django.contrib import admin
from .models import Store, Company, CustomerContact

members = [Store,  Company, CustomerContact]
admin.site.register(members)

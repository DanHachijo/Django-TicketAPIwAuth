from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    companyID = models.CharField(max_length=10, blank=True, null=True)
    street = models.CharField(max_length=100, blank=True, null=True)
    suite = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    zipcode = models.CharField(max_length=20, blank=True, null=True)

    memo = models.CharField(max_length=300, blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    is_customer = models.BooleanField(default=True)
    is_prospect = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name or ''


class Store(models.Model):
    company = models.ForeignKey(
        Company, on_delete=models.PROTECT, null=False, blank=False)
    name = models.CharField(max_length=30, null=True, blank=True)
    japanese_name = models.CharField(max_length=30, null=True, blank=True)
    storeID = models.CharField(max_length=10, null=True, blank=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    street = models.CharField(max_length=100, blank=True, null=True)
    suite = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    zipcode = models.CharField(max_length=20, blank=True, null=True)

    memo = models.CharField(max_length=300, blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    is_customer = models.BooleanField(default=True)
    is_prospect = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Stores'

    def __str__(self):
        return f"{self.name} "


class CustomerContact(models.Model):
    company = models.ForeignKey(
        Company, on_delete=models.PROTECT, null=True, blank=True)
    store = models.ForeignKey(
        Store, on_delete=models.PROTECT, blank=True, null=True)

    contact = models.CharField(max_length=30, blank=True, null=True)
    title = models.CharField(max_length=30, blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=60, blank=True, null=True)

    memo = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Customer Contacts'

    def __str__(self):
        return f"{self.contact} "

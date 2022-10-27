from django.db import models
# Importing the Member model and customers models
from members.models import Member
from customers.models import Store, CustomerContact, Company
from crum import get_current_user


class TicketCategory(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Ticket Categories'

    def __str__(self):
        return self.name


class Ticket(models.Model):
    category = models.ForeignKey(
        TicketCategory, on_delete=models.PROTECT, related_name="category_name")
    created_by = models.ForeignKey(
        'members.Member', on_delete=models.PROTECT, blank=True, null=True, default=None, related_name='ticket_created_by')
    updated_by = models.ForeignKey(
        'members.Member', on_delete=models.PROTECT, blank=True, null=True, default=None, related_name='ticket_updated_by') 
    ticket_date = models.DateTimeField(blank=True, null=True)

    is_open = models.BooleanField(default=False)
    is_email = models.BooleanField(default=False)
    complete_by = models.DateField(blank=True, null=True)
    open_details = models.CharField(max_length=100, null=True, blank=True)

    inquiry = models.CharField(max_length=1000)
    respond = models.CharField(max_length=1000)
  

  
    # Custromer Info
    company = models.ForeignKey(Company, on_delete=models.PROTECT, blank=True, null=True)
    store = models.ForeignKey(Store, on_delete=models.PROTECT, blank=True, null=True)

    is_contact = models.BooleanField(default=False)
    contact = models.ForeignKey(CustomerContact, on_delete=models.PROTECT, blank=True, null=True)

    contact_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Tickets'

    def __str__(self):
        return self.inquiry or ''

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.created_by = user
        self.updated_by = user
        super(Ticket, self).save(*args, **kwargs)

from tickets.views import TicketViewSet, CategoryViewSet
from members.views import MemberViewSet, OfficeViewSet
from customers.views import (
    StoreViewSet, 
    CompanyViewSet, 
    CustomerContactViewSet, 
    StoreViewSet,
)




from rest_framework import routers

router = routers.DefaultRouter()
# MEMBERS
router.register('office', OfficeViewSet)
router.register('staff', MemberViewSet)
# TICKET
router.register('tickets', TicketViewSet)
router.register('ticket-categories', CategoryViewSet)
# CUSTOMERS
router.register('company', CompanyViewSet)
router.register('store', StoreViewSet)
router.register('customer-contact', CustomerContactViewSet)

# urlpatterns = router.urls

from django.contrib import admin
from django.urls import path, include
from .router import router
from rest_framework.authtoken import views
from members.views import CustomAuthToken
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-token-auth/', CustomAuthToken.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

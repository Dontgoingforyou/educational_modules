from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Educational Modules API",
      default_version='v1',
      description="API для образовательных модулей",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@educationalmodules.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('modules.api_urls', namespace='modules')),
    path('users/', include('users.api_urls', namespace='users')),
    path('swagger/', schema_view.as_view(), name='swagger'),
]

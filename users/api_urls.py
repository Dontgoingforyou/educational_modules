from django.urls import path, include
from users.api_views import UserViewSet
from users.apps import UsersConfig
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r'', UserViewSet, basename='user')

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('<int:pk>/update_role/', UserViewSet.as_view({'patch': 'update_role'}), name='user-update-role'),
    path('', include(router.urls)),
]
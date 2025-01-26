from django.urls import path, include
from rest_framework.routers import DefaultRouter
from modules.api_views import EducationalModuleViewSet, LessonViewSet
from modules.apps import ModulesConfig

app_name = ModulesConfig.name

router = DefaultRouter()
router.register(r'modules', EducationalModuleViewSet, basename='module')
router.register(r'lessons', LessonViewSet, basename='lesson')

urlpatterns = [
    path('', include(router.urls)),
]
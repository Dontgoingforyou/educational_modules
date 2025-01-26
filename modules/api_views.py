from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from modules.models import EducationModule, Lesson
from modules.serializers import EducationalModuleSerializer, LessonSerializer


class EducationalModuleViewSet(viewsets.ModelViewSet):
    """
    Представление для управления образовательными модулями.
    Реализует CRUD операции и публикацию модуля.
    """

    queryset = EducationModule.objects.all()
    serializer_class = EducationalModuleSerializer
    filter_backends = (filters.OrderingFilter, filters.SearchFilter)
    search_fields = ['title', 'description']
    ordering_fields = ['order']
    ordering = ['order']

    @action(detail=True, methods=['post'])
    def publish(self, request, pk=None) -> Response:
        """ Публикация модуля."""

        module = self.get_object()
        if module.is_published:
            return Response({'status': 'Модуль уже опубликован'}, status=400)
        module.is_published = True
        module.save()
        return Response({'status': 'Модуль опубликован'})


class LessonViewSet(viewsets.ModelViewSet):
    """
    Представление для управления уроками.
    Реализует CRUD операции для уроков.
    """

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['module__title', 'title']
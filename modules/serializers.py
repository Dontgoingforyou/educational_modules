from rest_framework import serializers
from modules.models import EducationModule, Lesson
from typing import List


class LessonSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели урока.
    """

    class Meta:
        model = Lesson
        fields = '__all__'

class EducationalModuleSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели образовательного модуля.
    Включает вложенные данные по урокам.
    """

    lessons: List[LessonSerializer] = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = EducationModule
        fields = ['id', 'title', 'description', 'order', 'lessons']

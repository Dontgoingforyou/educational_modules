from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """
    Модель для кастомного пользователя с ролью.
    Роли могут быть 'admin', 'teacher', 'student'.
    """

    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    ]
    role: str = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')

    def __str__(self) -> str:
        """ Возвращает строковое представление объекта. """
        return f"{self.username} ({self.get_role_display()})"
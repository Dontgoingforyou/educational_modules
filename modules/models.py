from django.db import models


class EducationModule(models.Model):
    """
    Модель для образовательного модуля.
    Содержит информацию о порядке, названии и описании модуля.
    """

    order: int = models.PositiveIntegerField(verbose_name='Порядковый номер')
    title: str = models.CharField(max_length=255, verbose_name='Название')
    description: str = models.TextField(verbose_name='Описание')
    is_published: bool = models.BooleanField(default=False, verbose_name='Статус публикации')

    class Meta:
        verbose_name = 'Модуль'
        verbose_name_plural = 'Модули'
        ordering = ['order']

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.
        """
        return self.title


class Lesson(models.Model):
    """
    Модель для урока внутри образовательного модуля.
    Связан с модулем, имеет порядок и описание.
    """

    module: EducationModule = models.ForeignKey(EducationModule, on_delete=models.CASCADE, related_name='lessons')
    title: str = models.CharField(max_length=255, verbose_name='Название')
    description: str = models.TextField(verbose_name='Описание')
    order: int = models.PositiveIntegerField(verbose_name='Порядок уроков внутри модуля')

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        ordering = ['order']
        unique_together = ('module', 'order')

    def __str__(self) -> str:
        """ Возвращает строковое представление объекта. """
        return self.title

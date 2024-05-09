from django.db import models
from django.contrib.auth.models import AbstractUser
from .utilities import get_timestamp_path

class AdvUser(AbstractUser):
    send_messages = models.BooleanField(default=False, verbose_name='Следить за новыми рецептами?')

    def delete(self, *args, **kwargs):
        for rs in self.rs_set.all():
            rs.delete()
        super().delete(*args, **kwargs)

    class Meta(AbstractUser.Meta):
        pass

class Category(models.Model):
    name = models.CharField(max_length=20, db_index=True, unique=True, verbose_name='Название')
    order = models.SmallIntegerField(default=0, db_index=True, verbose_name='Порядок')

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('order', 'name')
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Rs(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория')
    title = models.CharField(max_length=40, verbose_name='Название')
    description = models.TextField(default='', verbose_name='Описание')
    cooking_steps = models.TextField(blank=True,default='', verbose_name='Шаги приготовления')
    cooking_time = models.PositiveIntegerField(default=1, verbose_name='Время приготовления')
    image = models.ImageField(blank=True, upload_to=get_timestamp_path, verbose_name='Изображение')
    author = models.ForeignKey(AdvUser, on_delete=models.CASCADE, verbose_name='Автор рецепта')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Добавлено')

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        ordering = ['-created_at']


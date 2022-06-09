from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(
        'Email', unique=True, max_length=254,
        help_text='Введите действительный адрес')
    username = models.CharField(
        'Имя пользователя', max_length=150, unique=True)

    class Meta:
        ordering = ('id', )
        verbose_name = 'пользователя'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

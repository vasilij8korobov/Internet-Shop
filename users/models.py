from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to='avatars/', **NULLABLE, verbose_name="Фото пользователя")
    phone_number = models.CharField(max_length=15, **NULLABLE, verbose_name="Телефон")
    country = models.CharField(max_length=100, **NULLABLE, verbose_name="Страна")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    def __str__(self):
        return self.email

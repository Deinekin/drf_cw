from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"blank": "True", "null": "True"}


class User(AbstractUser):
    """User's model class"""

    username = None
    email = models.EmailField(unique=True, verbose_name="Почта")
    chat_id = models.CharField(max_length=255, verbose_name="chat_id", **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

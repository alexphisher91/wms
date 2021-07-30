from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class TimeStamps(models.Model):
    """Дата и время создания, обновления"""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class OwnerModel(models.Model):
    """Автор сущьности"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True

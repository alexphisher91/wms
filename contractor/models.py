from django.db import models
from djangoProject.base_models import TimeStamps


class ContractorTypes(TimeStamps, models.Model):
    """Типы контрагентов"""
    name = models.CharField(max_length=100, unique=True, null=False)

    def __str__(self):
        return self.name


class Contractor(TimeStamps, models.Model):
    """Контрагенты"""
    name = models.CharField(max_length=100, unique=True, null=False)
    type = models.ForeignKey(ContractorTypes, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

from django.db import models
from djangoProject.base_models import TimeStamps, OwnerModel


class Product(OwnerModel, TimeStamps, models.Model):
    """Товары"""
    article = models.CharField(max_length=100, unique=True, null=False)
    name = models.CharField(max_length=100, unique=True, null=False)
    full_name = models.CharField(max_length=300)
    blocked = models.BooleanField(default=False)

    def __str__(self):
        """Код товара для представления"""
        return self.article


class UnitTypes(TimeStamps, models.Model):
    """Типы едениц хранения"""
    name = models.CharField(max_length=100, unique=True, null=False)

    def __str__(self):
        return self.name


class Unit(OwnerModel, TimeStamps, models.Model):
    """Еденица товара"""
    name = models.CharField(max_length=100, null=False)
    ratio = models.DecimalField(decimal_places=3, max_digits=3, null=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    width = models.DecimalField(decimal_places=3, max_digits=3, null=False)
    length = models.DecimalField(decimal_places=3, max_digits=3, null=False)
    height = models.DecimalField(decimal_places=3, max_digits=3, null=False)
    weight = models.DecimalField(decimal_places=3, max_digits=3, null=False)
    volume = models.DecimalField(decimal_places=3, max_digits=3, null=False)

    unit_type = models.ForeignKey(UnitTypes, on_delete=models.CASCADE, null=False)

    class Meta:
        """Уникальность единицы в пределах товара и кванта ... """
        unique_together = ('product', 'ratio')

    def __str__(self):
        return self.name

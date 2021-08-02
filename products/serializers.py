from rest_framework import serializers
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    article = serializers.CharField()
    name = serializers.CharField()

    class Meta:
        exclude = ['user']
        model = Product



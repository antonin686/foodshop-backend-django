from rest_framework import serializers
from shop.models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    icon = serializers.ImageField(use_url=True)
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Category
        fields = ['id', 'title', 'icon', 'slug', 'image', 'description']

class ProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Product
        fields = ['id', 'title', 'slug', 'price', 'image']

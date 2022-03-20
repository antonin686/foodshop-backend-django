from asyncore import read
from audioop import add
from pprint import pprint
from rest_framework import serializers
from shop.models import Product, Category, Customer, Address, OrderItem, Order


class SimpleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "title", "price", 'image'] 

class SimpleAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ["id", "address", "city", "post_code"] 

class CustomerSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Customer
        fields = ["id", "user_id", "birth_date", "membership"]


class AddressSerializer(serializers.ModelSerializer):
    customer_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Address
        fields = [
            "id",
            "customer_id",
            "name",
            "address",
            "company",
            "city",
            "post_code",
            "region",
        ]

class CategorySerializer(serializers.ModelSerializer):
    icon = serializers.ImageField(use_url=True)
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Category
        fields = ["id", "title", "icon", "slug", "image", "description"]


class ProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Product
        fields = ["id", "title", "slug", "price", "image"]

class OrderItemSerializer(serializers.ModelSerializer):
    product = SimpleProductSerializer()
    class Meta:
        model = OrderItem
        fields = ["id", "product", "quantity"]

class OrderSerializer(serializers.ModelSerializer):
    status = serializers.IntegerField()
    items = OrderItemSerializer(many=True)
    address = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ["id", "customer_id", "address", "status", "items", 'created_at']

    def get_address(self, obj):
        address = Address.objects.get(pk=obj.address_id)
        return SimpleAddressSerializer(address).data


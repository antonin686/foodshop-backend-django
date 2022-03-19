from audioop import add
from pprint import pprint
from rest_framework import serializers
from shop.models import Product, Category, Customer, Address


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

        # user_id = self.context["user_id"]
        # name = self.validated_data["name"]
        # address = self.validated_data["address"]
        # company = self.validated_data["company"]
        # city = self.validated_data["city"]
        # post_code = self.validated_data["post_code"]
        # region = self.validated_data["region"]
        # (customer, created) = Customer.objects.get_or_create(user_id=user_id)
        # addressobj = Address.objects.create(
        #     customer=customer,
        #     name=name,
        #     address=address,
        #     company=company,
        #     city=city,
        #     post_code=post_code,
        #     region=region,
        # )



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

from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from ..models import Address, Customer, Order, OrderItem
from ..serializers import AddressSerializer, OrderSerializer
from pprint import pprint
from rest_framework.decorators import api_view
from core.models import User
from django.contrib.auth.hashers import make_password


class AddressViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        return {"user_id": self.request.user.id}

    def create(self, request):
        user_id = request.user.id
        name = request.data["name"]
        address = request.data["address"]
        company = request.data["company"]
        city = request.data["city"]
        post_code = request.data["post_code"]
        region = request.data["region"]
        (customer, created) = Customer.objects.get_or_create(user_id=user_id)
        addressobj = Address.objects.create(
            customer=customer,
            name=name,
            address=address,
            company=company,
            city=city,
            post_code=post_code,
            region=region,
        )
        return Response("ok")

    @action(detail=False, permission_classes=[IsAuthenticated])
    def choices(self, request):
        choices = []
        for value, title in Address.REGION_CHOICES:
            choices.append({"label": title, "value": value})

        return Response(choices)


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request):
        # pprint(request.data['items'])
        user_id = request.user.id
        address_id = request.data["address"]
        items = request.data["items"]
        (customer, created) = Customer.objects.get_or_create(user_id=user_id)
        order = Order.objects.create(customer=customer, address_id=address_id)

        for item in request.data["items"]:
            OrderItem.objects.create(
                order=order, product_id=item["id"], quantity=item["quantity"]
            )

        return Response("ok")


@api_view(["POST"])
def register(request):
    first_name = request.data["first_name"]
    last_name = request.data["last_name"]
    username = request.data["username"]
    password = request.data["password"]
    phone = request.data["phone"]
    email = request.data["email"]

    User.objects.create(
        first_name=first_name,
        last_name=last_name,
        password=make_password(password),
        username=username,
        phone=phone,
        email=email,
    )

    return Response('ok')

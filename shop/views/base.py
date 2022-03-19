from secrets import choice
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from ..models import Address, Customer
from ..serializers import AddressSerializer
from pprint import pp, pprint
import json

from shop import serializers

class AddressViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer 
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        return {'user_id': self.request.user.id}

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
        return Response('ok')
        



    @action(detail=False, permission_classes=[IsAuthenticated])
    def choices(self, request):
        choices = []
        for value, title in Address.REGION_CHOICES:
            choices.append({"title": title, "value": value})
        

        return Response(choices)
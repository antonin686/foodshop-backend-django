from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Product
from ..serializers import ProductSerializer 
from pprint import pprint

@api_view()
def product_index(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True, context={"request":request})

    return Response(serializer.data)
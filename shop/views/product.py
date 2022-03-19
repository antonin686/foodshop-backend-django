from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Product
from ..serializers import ProductSerializer 
from pprint import pprint
import json

@api_view()
def product_index(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True, context={"request":request})

    return Response(serializer.data)

@api_view()
def product_query(request, query):
    if query == "popular":
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True, context={"request":request})
    return Response(serializer.data)

@api_view(['POST'])
def product_filter(request):
    body_unicode = request.body.decode('utf-8') 	
    body = json.loads(body_unicode) 	
    search = body['search']
    filters = body['filters']
    products = Product.objects.filter(title__contains=search)
    pprint(body)
    for f in filters:
        fk = f['fk']
        idx = []
        for item in f['items']:
            if item['checked']:
                idx.append(item['id'])
        if len(idx) > 0:
            products = products.filter(category_id__in=idx)
    #return Response(dir(request))
    #pprint(serializer.data)
    serializer = ProductSerializer(products, many=True, context={"request":request})

    return Response(serializer.data)
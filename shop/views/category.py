from re import search
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from ..models import Category
from ..serializers import CategorySerializer, ProductSerializer 

@api_view()
def category_index(request):
    category = Category.objects.all()
    serializer = CategorySerializer(category, many=True, context={"request":request})

    return Response(serializer.data)

@api_view()
def category_products(request, slug):
    category = get_object_or_404(Category, slug=slug)
    serializer = ProductSerializer(category.products, many=True, context={"request":request})
    
    return Response(serializer.data)
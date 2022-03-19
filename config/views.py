from django.http import HttpResponse

def welcome(request):
    return HttpResponse('Welcome to FoodShop Backend Created with Django by Md Antonin Islam')
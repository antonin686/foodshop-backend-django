from xml.etree.ElementInclude import include
from django.urls import path
from rest_framework.routers import SimpleRouter
from django.urls.conf import include
from . import views


router = SimpleRouter()

router.register('customers', views.CustomerViewSet)
router.register('addresses', views.AddressViewSet)
router.register('orders', views.OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('products/', views.product_index),
    path('products/query/<query>/', views.product_query),
    path('products/custom/filter', views.product_filter),
    path('products/query/categories/<slug:slug>', views.category_products),
    path('categories/', views.category_index),
    path('categories/<slug:slug>/products/', views.category_products),
]
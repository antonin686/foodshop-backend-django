from django.contrib import admin
from . import models

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_per_page = 10

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug' : ['title']
    }
    list_per_page = 10
    search_fields = ['title']

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug' : ['title']
    }
    autocomplete_fields = ['category']
    list_per_page = 10

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_per_page = 10

@admin.register(models.OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_per_page = 10

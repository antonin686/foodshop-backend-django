from email.policy import default
from pyexpat import model
from statistics import mode
from django.db import models 
from django.conf import settings
import os
import uuid

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('', filename)

class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD, 'Gold'),
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return self.user.username

class Address(models.Model):
    REGION_CHOICES = [
        (1, 'Dhaka'),
        (2, 'Rangpur'),
        (3, 'Khulna'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="addresses")
    name = models.CharField(max_length=255)
    company = models.CharField(max_length=255, null=True, blank=True)
    address = models.TextField()
    city = models.CharField(max_length=255)
    post_code = models.CharField(max_length=255)
    region = models.IntegerField(choices=REGION_CHOICES, default=1)

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(null=True)
    icon = models.ImageField(upload_to=get_file_path)
    image = models.ImageField(upload_to=get_file_path)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self) -> str:
        return self.title

class Product(models.Model):
    AVAILABILITY_CHOICES = [
        (0, 'NO'),
        (1, 'YES'),
    ]
    title = models.CharField(max_length=255)
    slug = models.SlugField(null=True)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to=get_file_path)
    availability = models.SmallIntegerField(choices=AVAILABILITY_CHOICES, default=1)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="products")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

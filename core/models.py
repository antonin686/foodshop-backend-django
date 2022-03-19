import imp
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

class User(AbstractUser):
    email = models.EmailField(unique=True, null=True, blank=True)
    phone_regex = RegexValidator(regex=r'^\d{11}$', message="Invalid Phone Number")
    phone = models.CharField(validators=[phone_regex], max_length=11, unique=True)

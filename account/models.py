from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    first_name: object = models.CharField(max_length=32)
    last_name: object = models.CharField(max_length=150)
    email: object = models.EmailField(unique=True)

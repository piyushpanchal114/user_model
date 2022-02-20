from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import EmailField


class User(AbstractUser):
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=255)
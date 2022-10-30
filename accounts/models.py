from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


from .managers import CustomUserManager


class CustomUser(AbstractUser):

    username = None
    
    email = models.EmailField(unique=True, verbose_name='Email Address')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
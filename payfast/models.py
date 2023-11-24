from django.db import models
from django.contrib.auth.models import AbstractUser
from payfast.manager import UserManager


class User(AbstractUser):
    email = models.EmailField(unique=True, blank=True, null=True)
    username = models.CharField(max_length=200, unique=True, blank=True, null=True)
    USERNAME_FIELD = 'email'
    phone = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)


    REQUIRED_FIELDS = ['username']
    objects = UserManager()

    def __str__(self):
        return self.email
    
    def get_full_name(self) -> str:
        return super().get_full_name()
    


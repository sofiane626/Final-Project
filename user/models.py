from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date

# Create your models here.

class Role(models.Model):
    value = models.CharField(max_length=50)
    def __str__(self):
        return self.value

class User(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.CASCADE, blank=True, null=True)
    img_url = models.CharField(max_length=250)
    is_subscribed = models.BooleanField(default=False)
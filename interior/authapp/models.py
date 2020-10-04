from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='img_users', blank=True)

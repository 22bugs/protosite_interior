from django.conf import settings

from django.db import models
from mainapp.models import Product


# Create your models here.

class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='user', null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, verbose_name='product', null=True, on_delete=models.SET_NULL)
    quantity = models.PositiveIntegerField(verbose_name='quantity', default=0)
    add_datetime = models.DateTimeField(auto_now_add=True)

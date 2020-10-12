from django.conf import settings

from django.db import models
from mainapp.models import Product


# Create your models here.

class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='user', null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, verbose_name='product', null=True, on_delete=models.SET_NULL)
    quantity = models.PositiveIntegerField(verbose_name='quantity', default=0)
    add_datetime = models.DateTimeField(auto_now_add=True)

    @property # позволяет обращаться не как к методу, а как к свойству
    def product_cost(self):
        return self.product.price * self.quantity
    
    @property
    def total_quantity(self):
        _items = Basket.objects.filter(user=self.user)
        _total_quantity = sum(list(map(lambda x: x.quantity, _items)))
        return _total_quantity
    
    @property
    def total_cost(self):
        _items = Basket.objects.filter(user=self.user)
        _total_cost = sum(list(map(lambda x: x.product_cost, _items)))
        return _total_cost

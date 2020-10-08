from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from mainapp.models import Product
from basketapp.models import Basket


# Create your views here.

def basket(request):
    pass

def basket_add(request, pk): # pk продукта
    prod_key = get_object_or_404(Product, pk=pk)
    basket_key = Basket.objects.filter(product=prod_key, user=request.user).first() # вернет None, если товара нет

    if not basket_key: # создаст товар, если его нет
        basket_key = Basket.objects.create(product=prod_key, user=request.user)
    
    basket_key.quantity += 1
    basket_key.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def basket_remove(request, pk): # pk корзины
    pass

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from mainapp.models import Product
from basketapp.models import Basket


# Create your views here.

@login_required # не сработает, если пользователь не залогинился. перекидывает на LOGIN_URL
def basket(request):
    bask_set = Basket.objects.filter(user=request.user)
    
    content = {
        'page_name': 'basket',

        'basket': bask_set,
    }

    return render(request, 'basketapp/basket.html', content)

@login_required
def basket_add(request, pk): # pk продукта
    prod_key = get_object_or_404(Product, pk=pk)
    basket_key = Basket.objects.filter(product=prod_key, user=request.user).first() # вернет None, если товара нет

    if not basket_key: # создаст товар, если его нет
        basket_key = Basket.objects.create(product=prod_key, user=request.user)
    
    basket_key.quantity += 1
    basket_key.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def basket_remove(request, pk): # pk корзинки
    basket_item = get_object_or_404(Basket, pk=pk)
    basket_item.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

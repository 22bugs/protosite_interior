import os
import json
from django.conf import settings
from django.shortcuts import render, get_object_or_404

from mainapp.models import *
from authapp.models import *
from basketapp.models import *


with open(os.path.join(settings.JSON_MAIN, 'navigation.json'), 'r', encoding='utf-8') as open_nav:
    load_nav = json.load(open_nav)


# Create your views here.

def index(request):
    content = {
        'page_name': 'home',

        'navigation': load_nav['menu'],
        'usefull': load_nav['usefull'],
        'socials': load_nav['socials'],
    }

    if request.user.is_authenticated:
        user_ava = ShopUser.objects.get(username=request.user).avatar
        bask_set = Basket.objects.filter(user=request.user)
    
        authenticated ={
            'avatar': user_ava,
            'basket': bask_set,
        }

        content.update(authenticated)

    return render(request, 'mainapp/index.html', content)


def products(request, pk=None):
    cats_set = ProductCategory.objects.all()

    if pk is not None:
        cat_key = get_object_or_404(ProductCategory, pk=pk) # выводит 404, если адрес не существует
        prod_set = Product.objects.filter(category=cat_key)[:6]
    else:
        prod_set = Product.objects.all().order_by('name')[:12]

    content = {
        'page_name': 'products',
        'head_name': 'our products range',

        'navigation': load_nav['menu'],
        'usefull': load_nav['usefull'],
        'socials': load_nav['socials'],
        'categories': cats_set,
        'products': prod_set,
    }

    if request.user.is_authenticated:
        user_ava = ShopUser.objects.get(username=request.user).avatar
        bask_set = Basket.objects.filter(user=request.user)
    
        authenticated ={
            'avatar': user_ava,
            'basket': bask_set,
        }

        content.update(authenticated)

    return render(request, 'mainapp/products.html', content)


def contact(request):
    cont_set = Contact.objects.all()

    content = {
        'page_name': 'contact',
        'head_name': 'contact us',

        'navigation': load_nav['menu'],
        'usefull': load_nav['usefull'],
        'socials': load_nav['socials'],
        'locations': cont_set,
    }

    if request.user.is_authenticated:
        user_ava = ShopUser.objects.get(username=request.user).avatar
        bask_set = Basket.objects.filter(user=request.user)
    
        authenticated ={
            'avatar': user_ava,
            'basket': bask_set,
        }

        content.update(authenticated)

    return render(request, 'mainapp/contact.html', content)

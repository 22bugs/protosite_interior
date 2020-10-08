import os
import json
from django.conf import settings
from django.shortcuts import render, get_object_or_404

from mainapp.models import *
from basketapp.models import *


with open(os.path.join(settings.JSON_MAIN, 'navigation.json'), 'r', encoding='utf-8') as open_nav:
    load_nav = json.load(open_nav)


# Create your views here.

def index(request):
    bask_set = sum(list(Basket.objects.filter(user=request.user).values_list('quantity', flat=True)))

    context = {
        'page_name': 'home',

        'navigation': load_nav['menu'],
        'usefull': load_nav['usefull'],
        'socials': load_nav['socials'],
        'basket': bask_set,
    }
    return render(request, 'mainapp/index.html', context)


def products(request, pk=None):
    bask_set = sum(list(Basket.objects.filter(user=request.user).values_list('quantity', flat=True)))

    cats_set = ProductCategory.objects.all()

    if pk is not None:
        cat_key = get_object_or_404(ProductCategory, pk=pk) # выводит 404, если адрес не существует
        prod_set = Product.objects.filter(category=cat_key)[:6]
    else:
        prod_set = Product.objects.all().order_by('name')[:12]

    context = {
        'page_name': 'products',
        'head_name': 'our products range',

        'navigation': load_nav['menu'],
        'usefull': load_nav['usefull'],
        'socials': load_nav['socials'],
        'categories': cats_set,
        'products': prod_set,
        'basket': bask_set,
    }
    return render(request, 'mainapp/products.html', context)


def contact(request):
    bask_set = sum(list(Basket.objects.filter(user=request.user).values_list('quantity', flat=True)))

    cont_set = Contact.objects.all()

    context = {
        'page_name': 'contact',
        'head_name': 'contact us',

        'navigation': load_nav['menu'],
        'usefull': load_nav['usefull'],
        'socials': load_nav['socials'],
        'locations': cont_set,
        'basket': bask_set,
    }
    return render(request, 'mainapp/contact.html', context)

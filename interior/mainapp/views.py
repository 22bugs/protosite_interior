import os
import json
from django.conf import settings
from django.shortcuts import render

from mainapp.models import ProductCategory, Product, Contact


with open(os.path.join(settings.JSON_MAIN, 'navigation.json'), 'r', encoding='utf-8') as open_nav:
    load_nav = json.load(open_nav)


# Create your views here.

def index(request):
    context = {
        'page_name': 'home',

        'navigation': load_nav['menu'],
        'extra_navigation': load_nav['extra_menu'],
        'usefull': load_nav['usefull'],
        'socials': load_nav['socials'],
    }
    return render(request, 'mainapp/index.html', context)


def products(request, category=None):
    cats_set = ProductCategory.objects.all()

    context = {
        'page_name': 'products',
        'head_name': 'our products range',

        'navigation': load_nav['menu'],
        'extra_navigation': load_nav['extra_menu'],
        'usefull': load_nav['usefull'],
        'socials': load_nav['socials'],
        'categories': cats_set,
    }
    return render(request, 'mainapp/products.html', context)


def contact(request):
    cont_set = Contact.objects.all()

    context = {
        'page_name': 'contact',
        'head_name': 'contact us',

        'navigation': load_nav['menu'],
        'extra_navigation': load_nav['extra_menu'],
        'usefull': load_nav['usefull'],
        'socials': load_nav['socials'],
        'locations': cont_set,
    }
    return render(request, 'mainapp/contact.html', context)

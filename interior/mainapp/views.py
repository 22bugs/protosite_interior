import os
import json

from django.conf import settings
from django.shortcuts import render

# Create your views here.

with open(os.path.join(settings.BASE_DIR, 'json/nav-pages.json'),
        'r',
        encoding='utf-8') as open_nav:
    load_nav = json.load(open_nav)

def index(request):
    context = {
        'page_name': 'home',

        'navigation': load_nav,
    }
    return render(request, 'mainapp/index.html', context)

def products(request):
    context = {
        'page_name': 'products',
        'head_name': 'our products range',

        'navigation': load_nav,
    }
    return render(request, 'mainapp/products.html', context)

def contact(request):
    context = {
        'page_name': 'contact',
        'head_name': 'contact us',

        'navigation': load_nav,
    }
    return render(request, 'mainapp/contact.html', context)

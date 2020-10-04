from django.urls import path

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name="index"),
    path('products/', mainapp.products, name="products"),
    path('products/<category>/', mainapp.products, name="category"),
    path('contact/', mainapp.contact, name="contact"),
]

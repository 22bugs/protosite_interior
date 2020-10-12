import os
import json
from django.conf import settings
from django.core.management import BaseCommand

from mainapp.models import ProductCategory, Product, Contact
from authapp.models import ShopUser


def load_json(file_name):
    with open(os.path.join(settings.JSON_MAIN, file_name + '.json'), 'r', encoding='utf-8') as json_file:
        return json.load(json_file)


class Command(BaseCommand):

    def handle(self, *args, **options):
        categories = load_json('db_categories')
        ProductCategory.objects.all().delete()
        for item in categories:
            ProductCategory.objects.create(**item)

        products = load_json('db_products')
        Product.objects.all().delete()
        for item in products:
            prod_cat = item['category']
            id_cat = ProductCategory.objects.get(name=prod_cat)
            item['category'] = id_cat
            Product.objects.create(**item)

        locations = load_json('db_locations')
        Contact.objects.all().delete()
        for item in locations:
            Contact.objects.create(**item)

        users = load_json('db_users')
        ShopUser.objects.all().delete()
        for item in users:
            ShopUser.objects.create(**item)

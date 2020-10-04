from django.db import models

from django.core.validators import RegexValidator

# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField(verbose_name='name', unique=True, max_length=64)
    description = models.TextField(verbose_name='desc.', blank=True, ) # blank=True может быть пустым

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(ProductCategory, verbose_name='category', null=True, on_delete=models.SET_NULL) # null возможен при удалении категории
    name = models.CharField(verbose_name='name', max_length=128)
    description = models.TextField(verbose_name='desc.', blank=True)
    short_description = models.CharField(verbose_name='short desc.', blank=True, max_length=64)
    image = models.ImageField(upload_to='img_products', blank=True)
    price = models.DecimalField(verbose_name='price', max_digits=8, decimal_places=2, default=0) # 8 разрядов из которых 2 десятичных
    quantity = models.PositiveIntegerField('quantity', default=0)
    status = models.CharField('status', max_length=32, blank=True)

    def __str__(self):
        return f'{self.name} --- {self.category.name}'

class Contact(models.Model):
    place = models.CharField(verbose_name='place', max_length=64)
    phone_regex = RegexValidator(regex=r'\d{3,4}\s-\s\d{3,4}\s-\s\d{3,4}')
    phone_number = models.CharField(verbose_name='phone', validators=[phone_regex], blank=True, max_length=18)
    email = models.EmailField(verbose_name='email', blank=True, max_length=64)
    address = models.CharField(verbose_name='address', blank=True, max_length=128)
    mapcode = models.CharField(verbose_name='mapcode', blank=True, max_length=512)

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'

    def __str__(self):
        return f'{self.place} --- {self.address}'

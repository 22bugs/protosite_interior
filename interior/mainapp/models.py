from django.db import models

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
    image = models.ImageField(upload_to='products_img', blank=True)
    price = models.DecimalField(verbose_name='price', max_digits=8, decimal_places=2, default=0) # 8 разрядов из которых 2 десятичных
    quantity = models.PositiveIntegerField('quantity', default=0)
    status = models.CharField('status', max_length=32, blank=True)

    def __str__(self):
        return f'{self.name} --- {self.category.name}'

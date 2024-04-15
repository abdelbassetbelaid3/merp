from django.db import models

# Create your models here.

class Categories(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='products/', blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField(default='')
    category_id = models.ForeignKey(Categories, on_delete=models.SET_NULL, null=True, blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2,default='0')
    cost = models.DecimalField(max_digits=12, decimal_places=2,default='0')
    category_id = models.IntegerField(default='1')
    class Meta:
        db_table = 'inventory_product'

class Products(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        db_table = 'products'

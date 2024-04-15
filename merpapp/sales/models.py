from django.db import models
from inventory.models import Product
# Create your models here.
class Locations(models.Model):
    location_id = models.AutoField(primary_key=True)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100,default=None,blank=True)
    state = models.CharField(max_length=100,default=None,blank=True)
    city = models.CharField(max_length=100,default=None,blank=True)
    country= models.CharField(max_length=100,default=None,blank=True)
    
class Customers(models.Model):
    customer_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=100)
    location_id = models.ForeignKey(Locations, on_delete=models.SET_NULL, null=True, blank=True)
class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_status = models.CharField(max_length=20)
    Customers_id = models.ForeignKey(Customers, on_delete=models.SET_NULL, null=True, blank=True)

class OrderItems(models.Model):
    order_item_id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(Customers, on_delete=models.SET_NULL, null=True, blank=True)
    product_id = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default='1')
    unit_price = models.IntegerField()
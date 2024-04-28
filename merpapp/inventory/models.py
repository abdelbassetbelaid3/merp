from django.db import models
from datetime import date
#from settings.models import Location
# Create your models here.

class Categories(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

class Vendor(models.Model):
    vendor_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=100)
    #location_id = models.ForeignKey(Location,on_delete=models.SET_NULL)
    shipping_cost = models.DecimalField(max_digits=12, decimal_places=2,default='0')
    lead_time = models.IntegerField()
    note = models.TextField()

class StorageLocation(models.Model):
    storage_location_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    shelf_number = models.IntegerField()
    level_number = models.IntegerField()
    storage_capacity = models.IntegerField()



    

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

class Inventory(models.Model):
    Inventory_id = models.AutoField(primary_key=True)
    location_id = models.ForeignKey(StorageLocation, on_delete=models.SET_NULL, null=True, blank=True)
    product_id = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField()
    # LOT NUMBER 

class InventoryTransaction(models.Model):
    inventory_transaction_id = models.AutoField(primary_key=True)
    date = models.DateField()
class Purchase_order(models.Model):
    purchase_order_id = models.AutoField(primary_key=True)
    order_date = models.DateField()
    recived_date = models.DateField()
    tracking_number = models.IntegerField()
    status = models.CharField(max_length=20)
    note = models.TextField()

class Purchase_items(models.Model):
    purchase_id = models.AutoField(primary_key=True)
    purchase_order_id = models.ForeignKey(Purchase_order, on_delete=models.SET_NULL, null=True, blank=True)
    product_id = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=12, decimal_places=2,default='0')
    
    



class Products(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        db_table = 'products'

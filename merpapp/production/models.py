from django.db import models
from inventory.models import Product

# Create your models here.
class billOfMaterial(models.Model):
    bom_id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    component_id = models.ForeignKey(Product, on_delete=models.SET_NULL,null= True , blank=True)
    quantity = models.IntegerField()
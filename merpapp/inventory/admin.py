from django.contrib import admin

# Register your models here.
from .models import Product , Products , Categories , Vendor , Purchase_order , Purchase_items

admin.site.register(Product)
admin.site.register(Products)
admin.site.register(Categories)
admin.site.register(Vendor)
admin.site.register(Purchase_order)
admin.site.register(Purchase_items)
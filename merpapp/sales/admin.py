from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Locations)
admin.site.register(Customers)
admin.site.register(Orders)
admin.site.register(OrderItems)
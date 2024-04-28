from django.urls import path
from . import views
urlpatterns = [
    path('inventory/',views.index,name='index'),
    path('purchase/',views.purchase,name='purchase'),
    path('newPurchase/',views.newPurchase,name='purchase'),
    path('vendors/',views.vendors,name='vendors'),
    path('vendors/newVendor',views.newVendor,name='vendors'),
    path('products/',views.products,name='products'),
    path('products/newProduct/',views.newProduct,name='newProduct'),
]

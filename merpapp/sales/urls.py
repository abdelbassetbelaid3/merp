from django.urls import path
from . import views
urlpatterns = [
    path('sales/',views.index,name='sales'),
    path('newCustomer/',views.newCustomer,name='newCustomer'),
    path('customers/',views.index,name='customers')
]
from django.shortcuts import render
from rest_framework.decorators import api_view, renderer_classes
from django.http import HttpResponse
from rest_framework.response import Response
from .models import *
from .serializers import *
# Create your views here.
@api_view(('GET',))
def index(request):
    orders = Orders.objects.all()
    locations = Locations.objects.all()
    customers = Customers.objects.all()
    serializerOrders = OrdersSerializer(orders, many=True)  # Serialize data
    serializerLocations = LocationsSerializer(locations, many=True)  # Serialize data
    serializerCustomers = CustomersSerializer(customers, many=True)  # Serialize data
    context = {
        'orders': serializerOrders.data ,
        'customers': serializerCustomers.data,
        'locations': serializerLocations.data,
        }
    return render(request,'sales/index.html',context) # Render data in template

def newCustomer(request):
    fullname = request.GET.get('FullName')
    address1 = request.GET.get('Address1')
    address2 = request.GET.get('Address2')
    city = request.GET.get('City')
    country = request.GET.get('Country')
    state = request.GET.get('State')
    location = Locations.objects.create(address1=address1,address2=address2,city=city,country=country,state=state)
    Customers.objects.create(full_name=fullname,location_id=location)
    context = {'data':address1}
    return render(request,'newCustomer.html',context)


def customers(request):

    locations = Locations.objects.all()
    customers = Customers.objects.all()
    serializerLocations = LocationsSerializer(locations, many=True)  # Serialize data
    serializerCustomers = CustomersSerializer(customers, many=True)  # Serialize data
    context = {
        'customers': serializerCustomers.data,
        'locations': serializerLocations.data,
        }  
    return render(request,'customers.html',context)




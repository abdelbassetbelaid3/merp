from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from .models import Product , Categories
from .serializers import ProductSerializer
from rest_framework.decorators import api_view, renderer_classes
# Create your views here.
@api_view(('GET',))
def index(request):
    products = Product.objects.all()  # Fetch all products from DB
    if Categories.objects.filter(name='uncategorized').exists():
        
        categories = Categories.objects.all()
    else:
        Categories.objects.create(category_id='1',name='uncategorized')
        categories = Categories.objects.all()


    serializer = ProductSerializer(products, many=True)  # Serialize data
    context = {'products': serializer.data} 
    return render(request,'index.html',context) # Render data in template
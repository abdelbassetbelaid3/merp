from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotFound, JsonResponse
from rest_framework.response import Response
from .models import Product , Categories, Vendor
from .serializers import ProductSerializer , CategorySerializer , VendorSerilaizer
from rest_framework.decorators import api_view, renderer_classes
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from django.http import HttpResponse
import xlsxwriter
import csv
from django.db import transaction

# Create your views here.
@api_view(('GET',))
def index(request):
    products = Product.objects.all()  # Fetch all products from DB
    
    if Categories.objects.filter(name='uncategorized').exists():
        
        pass
    else:
        Categories.objects.create(category_id='1',name='uncategorized')
        
    categories = Categories.objects.all()

    product_serializer = ProductSerializer(products, many=True)  # Serialize data
    category_serializer = CategorySerializer(categories, many=True)  # Serialize data

    context = {'products': product_serializer.data,'categories': category_serializer.data} 
    return render(request,'index.html',context) # Render data in template

def purchase(request):
    return render(request,'purchase.html')

def newPurchase(request):
    pass

def vendors(request):
    vendors = Vendor.objects.all()
    vendors_serialier = VendorSerilaizer(vendors,many = True)
    context = {'vendors':vendors_serialier.data}
    return render(request,'vendors.html',context)

def newVendor(request):
    pass

def products(request):
    products = Product.objects.all()  # Fetch all products from DB
    
    if Categories.objects.filter(name='uncategorized').exists():
        
        pass
    else:
        Categories.objects.create(category_id='1',name='uncategorized')
        
    categories = Categories.objects.all()

    product_serializer = ProductSerializer(products, many=True)  # Serialize data
    category_serializer = CategorySerializer(categories, many=True)  # Serialize data

    context = {'products': product_serializer.data,'categories': category_serializer.data} 
    return render(request,'products.html',context)


def newProduct(request):
    name = request.GET.get('name')
    price = request.GET.get('price')
    cost = request.GET.get('cost')
    image = request.GET.get('image')
    category = request.GET.get('category')
    print(name)
    
    Product.objects.create(price=price,name=name,cost=cost,image=image)
    context = {'data':price}
    return render(request,'newCustomer.html',context)

def importCsv(request):
    pass


def write_csv_data(data, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([field for field in data[0].keys()])  # Write header row
        for item in data:
            writer.writerow(item.values())  # Write data rows
def write_excel_data(data, filename):
    workbook = xlsxwriter.Workbook(filename)
    worksheet = workbook.add_worksheet()

    # Write header row
    for col, field in enumerate(data[0].keys()):
        worksheet.write(0, col, field)

    # Write data rows
    for row, item in enumerate(data, start=1):
        for col, value in enumerate(item.values()):
            worksheet.write(row, col, value)

    workbook.close()

# Example usage:
""" products = Product.objects.all().values('name', 'price', 'description')
write_excel_data(products, 'product_data.xlsx') """

def download_product_data(request):
    data_format = request.GET.get('format', 'csv')  # Allow user to choose CSV or Excel
    if data_format == 'csv':
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=product_data.csv'
        write_csv_data(Product.objects.all().values('name', 'price', 'description'), response)
    elif data_format == 'excel':
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=product_data.xlsx'
        write_excel_data(Product.objects.all().values('name', 'price', 'description'), response)
    else:
        response = HttpResponseNotFound()
    return response

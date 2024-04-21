from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from .models import Product , Categories
from .serializers import ProductSerializer
from rest_framework.decorators import api_view, renderer_classes
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas


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






def download_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="my_report.pdf"'

    # Create the PDF content using ReportLab
    p = canvas.Canvas(response)
    p.drawPath(stroke=1, fill=0, fillMode=None) 
    # Add your PDF content here (text, images, tables, etc.)
    p.drawString(100, 100, 'This is a sample PDF generated in Django!')

    p.showPage()
    p.save()

    return response
    
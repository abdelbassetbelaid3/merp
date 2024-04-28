from rest_framework import serializers
from .models import Product ,Categories , Vendor

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'  # Include all fields
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'  # Include all fields
class VendorSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'
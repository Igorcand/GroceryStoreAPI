from rest_framework import serializers
from product import models 

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product 
        fields = '__all__'

class ProductsClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductClasses 
        fields = '__all__'
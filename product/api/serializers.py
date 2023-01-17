from rest_framework import serializers
from product import models 

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product 
        fields = '__all__'
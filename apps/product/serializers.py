from rest_framework import serializers
from apps.product import models 

# O que é a serialização: é a conversão de objetos pyton para uma forma que facilite a integração com diferentes sistemas, o JSON. Então o serializer vai converter o model do python para json 
class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product 
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category 
        fields = '__all__'
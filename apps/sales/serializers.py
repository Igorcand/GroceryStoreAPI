from rest_framework import serializers
from apps.sales import models 

class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Sale 
        fields = '__all__'
from rest_framework import viewsets
from product.api import serializers
from product import models

class ProductsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ProductsSerializer
    queryset = models.Product.objects.all()
    
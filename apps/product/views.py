from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Category, Product
from .serializers import CategorySerializer, ProductsSerializer

class ProductAPIView(APIView):
    def get(self, request):
        produtos = Product.objects.all()
        serializer = ProductsSerializer(produtos, many=True)
        return Response(serializer.data)

class CategoryAPIView(APIView):
    def get(self, request):
        produtos = Category.objects.all()
        serializer = CategorySerializer(produtos, many=True)
        return Response(serializer.data)

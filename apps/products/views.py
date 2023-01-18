from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.response import JsonResponse
from django.http import Http404
from rest_framework.parsers import JSONParser 
from rest_framework import status 

from .models import Category, Product
from .serializers import CategorySerializer, ProductsSerializer

class ProductAPIView(APIView):
    def get(self, request):
        produtos = Product.objects.all()
        serializer = ProductsSerializer(produtos, many=True)
        return Response(serializer.data)

    def post(self, request):
        data =  JSONParser().parse(request)
        serializer = ProductsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductsSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductsSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CategoryAPIView(APIView):
    def get(self, request):
        produtos = Category.objects.all()
        serializer = CategorySerializer(produtos, many=True)
        return Response(serializer.data)

    def post(self, request):
        data =  JSONParser().parse(request)
        serializer = CategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        category = self.get_object(pk)
        try:
            category.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({"message":f"Cannot delete '{category}' because this category is been used"},status.HTTP_400_BAD_REQUEST)
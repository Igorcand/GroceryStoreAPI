from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated

from .models import Category, Product
from .serializers import CategorySerializer, ProductsSerializer


class ProductAPIView(APIView):
    # permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(tags=["Product"])
    def get(self, request):
        produtos = Product.objects.all()
        serializer = ProductsSerializer(produtos, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ProductsSerializer, tags=["Product"])
    def post(self, request):
        data = JSONParser().parse(request)
        serializer = ProductsSerializer(data=data)
        if serializer.is_valid():
            unit = serializer.validated_data.get("unit")
            if unit == None or unit == "Item":
                name = serializer.validated_data.get("name")
                description = serializer.validated_data.get("description")
                stock = serializer.validated_data.get("stock")
                price = serializer.validated_data.get("price")
                category = serializer.validated_data.get("category")

                stock = serializer.validated_data.get("stock")
                stock = int(stock)
                prod = Product(
                    name=name,
                    description=description,
                    stock=stock,
                    price=price,
                    category=category,
                )
                prod.save()
                serializer = ProductsSerializer(prod)
                return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
            else:
                serializer.save()
                return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailAPIView(APIView):
    # permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(tags=["Product"])
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise APIException("This product doesn't exist")

    @swagger_auto_schema(tags=["Product"])
    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductsSerializer(product)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ProductsSerializer, tags=["Product"])
    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductsSerializer(product, data=request.data)
        if serializer.is_valid():
            stock = serializer.validated_data.get("stock")
            if stock < 0:
                return Response(
                    {"message": f"Cannot update a negative stock."},
                    status.HTTP_400_BAD_REQUEST,
                )

            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(tags=["Product"])
    def delete(self, request, pk, format=None):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryAPIView(APIView):
    # permission_classes = (IsAuthenticated,)
    @swagger_auto_schema(tags=["Category"])
    def get(self, request):
        produtos = Category.objects.all()
        serializer = CategorySerializer(produtos, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=CategorySerializer, tags=["Category"])
    def post(self, request):
        data = JSONParser().parse(request)
        serializer = CategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetailAPIView(APIView):
    # permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(tags=["Category"])
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise APIException("This category doesn't exist")

    @swagger_auto_schema(tags=["Category"])
    def get(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    @swagger_auto_schema(tags=["Category"])
    def delete(self, request, pk, format=None):
        category = self.get_object(pk)
        try:
            category.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(
                {
                    "message": f"Cannot delete '{category}' because this category is been used."
                },
                status.HTTP_400_BAD_REQUEST,
            )

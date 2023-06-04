from django.http.response import JsonResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from src.apps.products.models import Category, Product
from src.apps.products.serializers import (
    CategorySerializer,
    ProductsSerializer,
)
from src.mixins.log import logger


class ProductAPIView(APIView):
    # permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(tags=['Product'])
    def get(self, request):
        try:
            produtos = Product.objects.all()
            serializer = ProductsSerializer(produtos, many=True)
            logger.info('Getting products')
            return Response(serializer.data)
        except Exception as e:
            logger.critical(f'{str(e)}')
            return Response(
                {'message': 'Something went wrong'},
                status.HTTP_400_BAD_REQUEST,
            )

    @swagger_auto_schema(request_body=ProductsSerializer, tags=['Product'])
    def post(self, request):
        data = JSONParser().parse(request)
        serializer = ProductsSerializer(data=data)
        if serializer.is_valid():
            unit = serializer.validated_data.get('unit')
            if unit is None or unit == 'Item':
                name = serializer.validated_data.get('name')
                description = serializer.validated_data.get('description')
                stock = serializer.validated_data.get('stock')
                price = serializer.validated_data.get('price')
                category = serializer.validated_data.get('category')

                stock = serializer.validated_data.get('stock')
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
                logger.info('Created item product successfully')
                return JsonResponse(
                    serializer.data, status=status.HTTP_201_CREATED
                )
            else:
                serializer.save()
                logger.info('Created kg product successfully')
                return JsonResponse(
                    serializer.data, status=status.HTTP_201_CREATED
                )
        logger.warning('Serializer is not valid')
        return JsonResponse(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


class ProductDetailAPIView(APIView):
    # permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(tags=['Product'])
    def get_object(self, pk):
        try:
            logger.info(f'Get product {pk}')
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            logger.warning("This product doesn't exist")
            raise APIException("This product doesn't exist")

    @swagger_auto_schema(tags=['Product'])
    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductsSerializer(product)
        logger.info(f'Get product {pk}')
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ProductsSerializer, tags=['Product'])
    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductsSerializer(product, data=request.data)
        if serializer.is_valid():
            stock = serializer.validated_data.get('stock')
            if stock < 0:
                logger.warning('Negative stock')
                return Response(
                    {'message': 'Cannot update a negative stock.'},
                    status.HTTP_400_BAD_REQUEST,
                )

            serializer.save()
            logger.info(f'Updated product {pk}')
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(tags=['Product'])
    def delete(self, request, pk, format=None):
        product = self.get_object(pk)
        product.delete()
        logger.info(f'Deleted product {pk}')
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryAPIView(APIView):
    # permission_classes = (IsAuthenticated,)
    @swagger_auto_schema(tags=['Category'])
    def get(self, request):
        produtos = Category.objects.all()
        serializer = CategorySerializer(produtos, many=True)
        logger.info('Getting categories')
        return Response(serializer.data)

    @swagger_auto_schema(request_body=CategorySerializer, tags=['Category'])
    def post(self, request):
        data = JSONParser().parse(request)
        serializer = CategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            logger.info('Created category')
            return JsonResponse(
                serializer.data, status=status.HTTP_201_CREATED
            )
        logger.warning('Serializer is not vailid')
        return JsonResponse(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


class CategoryDetailAPIView(APIView):
    # permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(tags=['Category'])
    def get_object(self, pk):
        try:
            logger.info(f'Get category {pk}')
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            logger.warning("This category doesn't exist")
            raise APIException("This category doesn't exist")

    @swagger_auto_schema(tags=['Category'])
    def get(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        logger.info(f'Get category {pk}')
        return Response(serializer.data)

    @swagger_auto_schema(tags=['Category'])
    def delete(self, request, pk, format=None):
        category = self.get_object(pk)
        try:
            category.delete()
            logger.info(f'Deleted category {pk}')
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            logger.warning(
                "You're trying to delete a category that its been used"
            )
            return Response(
                {
                    'message': f"Cannot delete '{category}' because this category is been used."
                },
                status.HTTP_400_BAD_REQUEST,
            )

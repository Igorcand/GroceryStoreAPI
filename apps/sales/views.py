from django.shortcuts import render

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.response import JsonResponse
from django.http import Http404
from rest_framework.parsers import JSONParser 
from rest_framework import status 

from .models import Sale, Product
from .serializers import SalesSerializer
from apps.reports.models import Reports

class SaleAPIView(APIView):
    def get(self, request):
        sales = Sale.objects.all()
        serializer = SalesSerializer(sales, many=True)
        return Response(serializer.data)

    def post(self, request):
        data =  JSONParser().parse(request)
        serializer = SalesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            quantity = serializer.validated_data.get('quantity')
            product_name = serializer.validated_data.get('product')
            data = serializer.validated_data.get('data')
            payment = serializer.validated_data.get('payment')

            product = Product.objects.get(name = product_name)
            stock = int(product.quantity)
            new_stock = stock - int(quantity)
            if new_stock < 0:
                return Response({"message":f"Cannot buy '{quantity}'  of '{product_name}' because we just have {stock} on stock"},status.HTTP_400_BAD_REQUEST)
            else:
                sale_price = int(quantity) * float(product.price)
                report = Reports(product=product_name, category=product.category, payment=payment, quantity_itens=quantity, stock=new_stock, sale=sale_price, data=data)
                report.save()
                product.quantity = new_stock
                product.save()


            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
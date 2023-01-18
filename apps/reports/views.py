from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser 
from rest_framework import status 
from drf_yasg.utils import swagger_auto_schema

from .models import Reports
from .serializers import ReportsSerializers


class ReportsAPIView(APIView):
    def get(self, request):
        reports = Reports.objects.all()
        serializer = ReportsSerializers(reports, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ReportsSerializers)
    def post(self, request):
        data =  JSONParser().parse(request)
        if 'data' in data.keys():
            reports = Reports.objects.filter(data=data['data'])
            if 'product' in data.keys():
                reports = reports.filter(product=data['product'])
            if 'category' in data.keys():
                reports = reports.filter(category=data['category'])
            if 'payment' in data.keys():
                reports = reports.filter(payment=data['payment'])

            serializer = ReportsSerializers(reports, many=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"message":f"You need to pass even 'data' value to do a filter on database"},status.HTTP_400_BAD_REQUEST)
        
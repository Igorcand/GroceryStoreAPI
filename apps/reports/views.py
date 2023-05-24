from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Reports
from .serializers import ReportsSerializers


class ReportsAPIView(APIView):
    # permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(tags=['Report'])
    def get(self, request):
        reports = Reports.objects.all()
        serializer = ReportsSerializers(reports, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ReportsSerializers, tags=['Report'])
    def post(self, request):
        data = JSONParser().parse(request)
        if 'data' in data.keys():
            reports = Reports.objects.filter(data__startswith=data['data'])
            if 'product' in data.keys():
                reports = reports.filter(product=data['product'])
            if 'category' in data.keys():
                reports = reports.filter(category=data['category'])
            if 'payment' in data.keys():
                reports = reports.filter(payment=data['payment'])

            serializer = ReportsSerializers(reports, many=True)
            description = serializer.data
            total_items = 0
            total_value = 0
            for descript in description:
                total_items += descript['quantity_itens']
                total_value += float(descript['sale'])

            response = {
                'data': {
                    'total_items': total_items,
                    'total_value': total_value,
                },
                'description': description,
            }

            return Response(response, status=status.HTTP_201_CREATED)
        return Response(
            {
                'message': "You need to pass even 'data' value to do a filter on database"
            },
            status.HTTP_400_BAD_REQUEST,
        )

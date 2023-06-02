from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from src.apps.authorization.tasks import test_func


class AuthorizationAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(tags=['Authorization'])
    def get(self, request):
        return Response(
            {'message': 'You have authorization.'},
            status.HTTP_200_OK,
        )


class CeleryAPIView(APIView):
    @swagger_auto_schema(tags=['Celery'])
    def get(self, request):
        test_func.delay()
        return Response(
            {'message': 'Done'},
            status.HTTP_200_OK,
        )

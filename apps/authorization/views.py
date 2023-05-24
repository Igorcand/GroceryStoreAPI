from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from .tasks import test_func


class AuthorizationAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(tags=['Authorization'])
    def get(self, request):
        return Response(
            {'message': f'You have authorization.'},
            status.HTTP_200_OK,
        )


class CeleryAPIView(APIView):
    @swagger_auto_schema(tags=['Celery'])
    def get(self, request):
        test_func.delay()
        return Response(
            {'message': f'Done'},
            status.HTTP_200_OK,
        )

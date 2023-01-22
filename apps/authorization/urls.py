from django.urls import path

from .views import (
    AuthorizationAPIView, CeleryAPIView
)

urlpatterns = [
    path("authorization/", AuthorizationAPIView.as_view(), name="authorization"),
    path("celery/", CeleryAPIView.as_view(), name="celery"),
]

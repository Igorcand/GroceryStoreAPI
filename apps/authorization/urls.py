from django.urls import path

from .views import (
    AuthorizationAPIView,
)

urlpatterns = [
    path("authorization/", AuthorizationAPIView.as_view(), name="authorization"),

]

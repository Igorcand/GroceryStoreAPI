from django.urls import path

from .views import SaleAPIView

urlpatterns = [
    path('sales/', SaleAPIView.as_view(), name='sales'),
]

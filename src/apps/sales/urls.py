from django.urls import path

from src.apps.sales.views import SaleAPIView

urlpatterns = [
    path('sales/', SaleAPIView.as_view(), name='sales'),
]

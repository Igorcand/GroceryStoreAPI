from django.urls import path

from .views import ReportsAPIView

urlpatterns = [
    path('reports/', ReportsAPIView.as_view(), name='reports'),
]

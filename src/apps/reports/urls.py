from django.urls import path

from src.apps.reports.views import ReportsAPIView

urlpatterns = [
    path('reports/', ReportsAPIView.as_view(), name='reports'),
]

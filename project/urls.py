from django.contrib import admin
from django.urls import path, include 



urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
    path('api/', include('apps.products.urls')),
    path('api/', include('apps.sales.urls')),
    path('api/', include('apps.reports.urls')),
    ]

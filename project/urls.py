from django.contrib import admin
from django.urls import path, include 
from django.views.generic import TemplateView

from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='Pastebin API', description='')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
    path('api/', include('apps.products.urls')),
    path('api/', include('apps.sales.urls')),
    path('api/', include('apps.reports.urls')),
    path('api_schema/', schema_view, name='api_schema'),
    path('docs/', TemplateView.as_view(
        template_name='docs.html',
        extra_context={'schema_url':'api_schema'}
        ), name='swagger-ui')
    ]

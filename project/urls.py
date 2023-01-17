from django.contrib import admin
from django.urls import path, include 


from rest_framework import routers
from product.api import viewsets as productsviewset

route = routers.DefaultRouter()
route.register(r'products', productsviewset.ProductsViewSet, basename='products')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)),
    path('api-auth', include('rest_framework.urls'))
    ]

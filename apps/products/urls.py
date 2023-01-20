from django.urls import path
from django.views.decorators.cache import cache_page

from .views import (
    ProductAPIView,
    ProductDetailAPIView,
    CategoryAPIView,
    CategoryDetailAPIView,
)

urlpatterns = [
    path("products_cache/", cache_page(60)(ProductAPIView.as_view()), name="products_cache"),
    path("products/", ProductAPIView.as_view(), name="products"),
    path("products/<int:pk>/", ProductDetailAPIView.as_view(), name="products_detail"),
    path("categories/", CategoryAPIView.as_view(), name="categories"),
    path(
        "categories/<int:pk>/",
        CategoryDetailAPIView.as_view(),
        name="categories_detail",
    ),
]

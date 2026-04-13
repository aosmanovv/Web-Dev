from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

#router = DefaultRouter()
#router.register('categories', CategoryViewSet, basename='categories')
#router.register('products', ProductViewSet, basename='products')


urlpatterns = [
    path('products/', ProductListAPIView.as_view()),
    path('products/<int:product_id>/', ProductDetailAPIView.as_view()),

    path('categories/', CategoryListAPIView.as_view()),
    path('categories/<int:pk>/', CategoryDetailAPIView.as_view()),
    path('categories/<int:pk>/products/', CategoryProductsAPIView.as_view()),
]
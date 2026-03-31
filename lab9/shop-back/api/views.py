from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # GET /api/categories/<id>/products/
    @action(detail=True, methods=['get'])
    def products(self, request, pk=None):
        category = self.get_object()
        qs = category.products.all()
        serializer = ProductSerializer(qs, many=True)
        return Response(serializer.data)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
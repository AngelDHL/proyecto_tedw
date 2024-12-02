from rest_framework import viewsets

from core.models import Category, Product, ProductImages, ProductReview, Vendor
from core.permissions import IsAdminOrReadOnly
from core.serializers import (
    CategorySerializer,
    ProductImagesSerializer,
    ProductReviewSerializer,
    ProductSerializer,
    VendorSerializer,
)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly]


class ProductImagesViewSet(viewsets.ModelViewSet):
    queryset = ProductImages.objects.all()
    serializer_class = ProductImagesSerializer
    permission_classes = [IsAdminOrReadOnly]


class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    permission_classes = [IsAdminOrReadOnly]


class ProductReviewViewSet(viewsets.ModelViewSet):
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer
    permission_classes = [IsAdminOrReadOnly]

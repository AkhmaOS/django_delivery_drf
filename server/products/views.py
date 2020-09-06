from django.db.models import Q
from django.http import HttpResponseBadRequest
from django.shortcuts import render
from rest_framework.generics import ListAPIView

from .models import ProductCategory, Product, ProductImage
from .serializers import ProductCategorySerializer, ProductsSerializer, ProductSerializer, ProductImageSerializer


class ProductCategoryView(ListAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


class ProductsView(ListAPIView):
    serializer_class = ProductsSerializer

    def get_queryset(self):
        category = self.kwargs['category_id']

        if category is not None:
            queryset = Product.objects.filter(category=category)
            return queryset
        else:
            return HttpResponseBadRequest


class ProductView(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category = self.kwargs['category_id']
        product = self.kwargs['product_id']

        if category is not None:
            queryset = Product.objects.filter(Q(category=category) & Q(id=product))
            return queryset
        else:
            return HttpResponseBadRequest

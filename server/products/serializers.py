from rest_framework import serializers
from .models import ProductCategory, Product, ProductImage
from server.tuteda import settings


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = ProductImage
        fields = ('id', 'image',)


class ProductSerializer(serializers.ModelSerializer):
    category = ProductCategorySerializer()
    product_image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'is_popular', 'category', 'product_image')

    @staticmethod
    def get_product_image(obj):
        image = obj.product.all()
        response = ProductImageSerializer(image, many=True).data
        return response

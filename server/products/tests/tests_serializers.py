from django.test import TestCase

from ..models import ProductCategory, Product, ProductImage
from ..serializers import ProductCategorySerializer, ProductSerializer, ProductImageSerializer


class ProductSerializersTest(TestCase):

    def setUp(self):
        self.product_category_data = {
            'name': 'TestCategory',
        }
        self.product_category = ProductCategory.objects.create(**self.product_category_data)
        self.product_category_serializer = ProductCategorySerializer(instance=self.product_category)

        self.product_data = {
            'name': 'Test',
            'category': self.product_category,
            'description': 'test',
            'price': '0',
        }
        self.product = Product.objects.create(**self.product_data)
        self.product_serializer = ProductSerializer(instance=self.product)

        self.product_image_data = {
            'product': self.product,
            'image': None,
        }

        self.product_image = ProductImage.objects.create(**self.product_image_data)
        self.product_image_serializer = ProductImageSerializer(instance=self.product_image)

    def test_product_category_serializer(self):
        data = self.product_category_serializer.data
        self.assertEqual(set(data.keys()), {'id', 'name'})

    def test_product_serializer(self):
        data = self.product_serializer.data
        self.assertEqual(set(data.keys()), {'id', 'name',
                                            'category', 'description',
                                            'price', 'product_image', 'is_popular'})

    def test_product_image_serializer(self):
        data = self.product_image_serializer.data
        self.assertEqual(set(data.keys()), {'id', 'image'})

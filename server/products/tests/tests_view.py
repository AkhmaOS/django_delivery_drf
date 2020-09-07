from django.test import TestCase
from django.urls import reverse

from ..views import ProductCategory, Product


class ProductsTest(TestCase):

    def setUp(self):
        ProductCategory.objects.create(
            name='TestCategory'
        )
        self.category = ProductCategory.objects.first()

        Product.objects.create(
            name='TestProduct',
            description='test',
            category=self.category,
            price=0,
            is_popular=False
        )
        self.product = Product.objects.filter(category=self.category).first()

    def test_products_view(self):
        resp = self.client.get(reverse('products', kwargs={'category_id': self.category.pk}))
        self.assertEqual(resp.status_code, 200)

    def test_product_view(self):
        resp = self.client.get(
            reverse('product', kwargs={'category_id': self.category.id, 'product_id': self.product.id}))
        self.assertEqual(resp.status_code, 200)

    def test_product_category_view(self):
        resp = self.client.get(reverse('product-category'))
        self.assertEqual(resp.status_code, 200)

    def test_product_popular_view(self):
        resp = self.client.get(reverse('product-popular'))
        self.assertEqual(resp.status_code, 200)

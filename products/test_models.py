from django.test import TestCase
from .models import Product, ProductType


class TestModels(TestCase):

    def test_product_string_method_returns_name(self):
        product = Product.objects.create(name='Test Product',
                                         product_code='1234',
                                         product_description='Test',
                                         price_current=123)
        self.assertEqual(str(product), 'Test Product')

    def test_product_type_string_method_returns_name(self):
        product_type = ProductType.objects.create(name='Test Product Type')
        self.assertEqual(str(product_type), 'Test Product Type')

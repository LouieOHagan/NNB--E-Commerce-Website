from django.test import TestCase
from .apps import ProductsConfig


class TestApps(TestCase):

    def test_products_apps(self):
        self.assertEqual(ProductsConfig.name, 'products')

from django.test import TestCase
from .apps import CartConfig


class TestApps(TestCase):

    def test_cart_apps(self):
        self.assertEqual(CartConfig.name, 'cart')

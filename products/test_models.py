from django.test import TestCase
from .models import Product, ProductType, ProductReview
from django.contrib.auth.models import User


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

    def test_product_review_string_method_returns_name(self):
        product = Product.objects.create(name='Test Product',
                                         product_code='1234',
                                         product_description='Test',
                                         price_current=123)

        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()

        product_review = ProductReview.objects.create(user=user,
                                                      product=product,
                                                      rating='5',
                                                      title='Test review',)
        self.assertEqual(str(product_review), 'Test review')

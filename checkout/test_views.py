from django.test import TestCase
from .models import Order
from products.models import Product


class TestViews(TestCase):

    def test_get_checkout_page_without_cart(self):
        response = self.client.get('/checkout/')
        self.assertRedirects(response, '/products/')

    def test_get_checkout_page(self):
        product = Product.objects.create(name='Test Product',
                                         product_code='1234',
                                         product_description='Test',
                                         price_current=123)
        response = self.client.post(f'/cart/add/{product.id}/', {
            'quantity': 1,
            'redirect_url': f'/products/{product.id}/'})

        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout.html')

    def test_checkout_success(self):
        order = Order.objects.create(full_name='Test',
                                     email_address='test@test,com',
                                     street_address1='Test',
                                     town_or_city='Test',
                                     country='Test',
                                     total=100,
                                     delivery_cost=0,
                                     grand_total=100,
                                     original_cart='{"5": 1}',
                                     stripe_pid='Test',)

        response = self.client.get(f'/checkout/checkout_success/{order.order_number}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout_success.html')

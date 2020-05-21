from django.test import TestCase
from .models import Order, OrderProduct
from products.models import Product


class TestModels(TestCase):

    def test_order_string_method_returns_name(self):
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

        self.assertEqual(str(order), order.order_number)

    def test_order_product_string_method_returns_name(self):
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

        product = Product.objects.create(name='Test Product',
                                         product_code='1234',
                                         product_description='Test',
                                         price_current=123)

        order_product = OrderProduct.objects.create(order=order,
                                                    product=product,
                                                    quantity=1,
                                                    product_cost=100)

        self.assertEqual(str(order_product), f'Product Code {product.product_code} \
            on order {order.order_number}')

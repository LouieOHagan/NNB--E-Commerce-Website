from django.test import TestCase
from products.models import Product


class TestViews(TestCase):

    def test_view_cart(self):
        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart/cart.html')

    def test_add_to_cart(self):
        product = Product.objects.create(name='Test Product',
                                         product_code='1234',
                                         product_description='Test',
                                         price_current=123)
        response = self.client.post(f'/cart/add/{product.id}/', {'quantity': 1, 'redirect_url': f'/products/{product.id}/'})
        self.assertRedirects(response, f'/products/{product.id}/')

    def test_update_cart(self):
        product = Product.objects.create(name='Test Product',
                                         product_code='1234',
                                         product_description='Test',
                                         price_current=123)
        self.client.post(f'/cart/add/{product.id}/', {'quantity': 1, 'redirect_url': f'/products/{product.id}/'})
        response = self.client.post(f'/cart/update/{product.id}/', {'quantity': 3,})
        cart = self.client.session['cart']
        self.assertEqual(cart['1'], 3)
        self.assertRedirects(response, f'/cart/')

    # def test_remove_item_from_cart(self):
    #     product = Product.objects.create(name='Test Product',
    #                                      product_code='1234',
    #                                      product_description='Test',
    #                                      price_current=123)
    #     response = self.client.get(f'/cart/remove/{product.id}/')
    #     self.assertEqual(self.client.session.pop(f'{product.id}'))
    #     self.assertRedirects(response, f'/cart/')

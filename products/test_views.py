from django.test import TestCase
from .models import Product, ProductType


class TestViews(TestCase):

    def test_display_products(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products-page.html')

    def test_display_products_by_category(self):
        product_type = ProductType.objects.create(name='Test Product Type')
        response = self.client.get(f'/products/?product_type= \
            {product_type.name}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products-page.html')

    def test_sorting_products_by_price(self):
        product_type = ProductType.objects.create(name='Test Product Type')
        sort_by = 'price_current'
        order_direction = 'asc'
        response = self.client.get(f'/products/?product_type={product_type.name} \
            &sort={sort_by}&direction={order_direction}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products-page.html')

    def test_sorting_products_by_name(self):
        product_type = ProductType.objects.create(name='Test Product Type')
        sort_by = 'name'
        order_direction = 'desc'
        response = self.client.get(f'/products/?product_type={product_type.name} \
            &sort={sort_by}&direction={order_direction}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products-page.html')

    def test_searching_products(self):
        searched_item = 'iPad'
        response = self.client.get(f'/products/?q={searched_item}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products-page.html')

    def test_individual_product_pages(self):
        product = Product.objects.create(name='Test Product',
                                         product_code='1234',
                                         product_description='Test',
                                         price_current=123)
        response = self.client.get(f'/products/{product.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/individual-product.html')

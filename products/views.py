from django.shortcuts import render

from .models import Product, ProductType


def display_products(request):
    all_products = Product.objects.all()
    product_type = None

    if request.GET:
        if 'product_type' in request.GET:
            product_type = request.GET['product_type'].split(',')
            all_products = all_products.filter(category__name__in=product_type)
            product_type = ProductType.objects.filter(name__in=product_type)

    context = {
        'products': all_products,
        'product_type': product_type,
    }

    return render(request, "products/products-page.html", context)

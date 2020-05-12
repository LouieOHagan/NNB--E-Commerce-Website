from django.shortcuts import render

from .models import Product


def display_products(request):
    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, "products/products-page.html", context)

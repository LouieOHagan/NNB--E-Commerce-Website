from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.db.models import Q

from .models import Product, ProductType


def display_products(request):
    all_products = Product.objects.all()
    product_type = None
    query = None

    if request.GET:
        if 'product_type' in request.GET:
            product_type = request.GET['product_type'].split(',')
            all_products = all_products.filter(category__name__in=product_type)
            product_type = ProductType.objects.filter(name__in=product_type)

        if 'q' in request.GET:
            query = request.GET['q']
            query_results = Q(name__icontains=query) | \
                Q(product_code__exact=query) | \
                Q(product_description__icontains=query)

            all_products = all_products.filter(query_results)

    context = {
        'products': all_products,
        'product_type': product_type,
        'search_content': query,
    }

    return render(request, "products/products-page.html", context)

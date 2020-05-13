from django.shortcuts import render
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, ProductType


def display_products(request):
    all_products = Product.objects.all()
    product_type = None
    query = None
    sort_by = None
    order_direction = None

    if request.GET:
        if 'product_type' in request.GET:
            product_type = request.GET['product_type'].split(',')
            all_products = all_products.filter(category__name__in=product_type)
            product_type = ProductType.objects.filter(name__in=product_type)

        if 'sort' in request.GET:
            sort_by = request.GET['sort']

            if sort_by == "name":
                sort_by = 'lower_name'
                all_products = all_products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                order_direction = request.GET['direction']
                if order_direction == "desc":
                    sort_by = f'-{sort_by}'

            all_products = all_products.order_by(sort_by)

        sorted_by = f'{sort_by}_{order_direction}'

        if 'q' in request.GET:
            query = request.GET['q']
            query_results = Q(name__icontains=query) | \
                Q(product_code__exact=query) | \
                Q(product_description__icontains=query)

            all_products = all_products.filter(query_results)

    context = {
        'products': all_products,
        'product_type': product_type,
        'sorted_by': sorted_by,
        'search_content': query,
    }

    return render(request, "products/products-page.html", context)

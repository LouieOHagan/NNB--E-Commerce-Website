from django.shortcuts import render
from django.db.models import Q

from .models import Product, ProductType


def display_products(request):
    all_products = Product.objects.all()
    product_type = None
    query = None
    sort_by = None
    direction = None

    if request.GET:
        if 'product_type' in request.GET:
            product_type = request.GET['product_type'].split(',')
            all_products = all_products.filter(category__name__in=product_type)
            product_type = ProductType.objects.filter(name__in=product_type)

        if 'sort' in request.GET:
            sort_by = request.GET['sort']

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == "desc":
                    sort_by = f'-{sort_by}'

            all_products = all_products.order_by(sort_by)

        if 'q' in request.GET:
            query = request.GET['q']
            query_results = Q(name__icontains=query) | \
                Q(product_code__exact=query) | \
                Q(product_description__icontains=query)

            all_products = all_products.filter(query_results)

    current_sorting = f'{sort_by}_{direction}'

    context = {
        'products': all_products,
        'product_type': product_type,
        'search_content': query,
        'sorted_by': current_sorting
    }

    return render(request, "products/products-page.html", context)

from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, ProductType, ProductReview
from .forms import ReviewForm


def display_products(request):
    """ display_products view is used to render the products page and
    display all products to page. It also takes care of the search/querying
    functionality and the sorting products by functionality
    """

    all_products = Product.objects.all()
    product_type = None
    query = None
    sort_by = None
    order_direction = None
    sorted_by = None

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


def indiv_products(request, product_id):
    """ indiv_products view renders individual product pages
    which displays more information about each product.
    """
    product_info = get_object_or_404(Product, pk=product_id)
    reviews = ProductReview.objects.filter(product=product_id)
    reviews = reviews.order_by(f'-date_posted')

    context = {
        'product': product_info,
        'reviews': reviews,
    }

    return render(request, 'products/individual-product.html', context)


def add_review(request, product_id):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, pk=product_id)
        if request.method == 'POST':
            form = ReviewForm(request.POST or None)
            if form.is_valid():
                data = form.save(commit=False)
                data.user = request.user
                data.display_name = request.POST['display_name']
                data.product = product
                data.rating = request.POST['rating']
                data.title = request.POST['title']
                data.product_review = request.POST['product_review']
                data.save()
                return redirect('indiv_products', product_id)
        else:
            form = ProductReview()

        context = {
            'form': form
        }
        return redirect('indiv_products', context)
    else:
        return redirect('account_login')


def edit_review(request, product_id, review_id):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, pk=product_id)
        review = ProductReview.objects.get(product=product, pk=review_id)

        if request.user == review.user:
            if request.method == 'POST':
                form = ReviewForm(request.POST, instance=review)
                if form.is_valid():
                    data = form.save(commit=False)
                    data.save()
                    return redirect('indiv_products', product_id)
            else:
                form = ReviewForm(instance=review)

            context = {
                'form': form,
                'product': product,
            }
            return render(request, 'products/edit_review.html', context)
        else:
            return redirect('indiv_products', product_id)
    else:
        return redirect('account_login')


def delete_review(request, product_id, review_id):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, pk=product_id)
        review = ProductReview.objects.get(product=product, pk=review_id)

        if request.user == review.user:
            review.delete()
        return redirect('indiv_products', product_id)
    else:
        return redirect('account_login')

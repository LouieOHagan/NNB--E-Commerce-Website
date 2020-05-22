from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from products.models import Product


def view_cart(request):
    """ view_cart view renders the cart page.
    It displays the items in the users cart
    """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ add_to_cart view is used to add an item and
    its specified quantity to the users cart and then
    ensures they are redirected to that items page
    """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.success(request, f'Updated quantity of {product.name} \
            to {cart[item_id]}')
    else:
        cart[item_id] = quantity
        messages.success(request, f'Added {product.name} to your cart!')

    request.session['cart'] = cart

    return redirect(redirect_url)


def update_cart(request, item_id):
    """ update_cart view is used to update the quantity
    of an item in the users cart. The user can update
    the quantity from 1 - 49
    """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
        messages.success(request, f'Updated quantity of {product.name} \
            to {cart[item_id]}')
    else:
        cart.pop(item_id)
        messages.success(request, f'Removed {product.name} from your cart')

    request.session['cart'] = cart

    return redirect(reverse('view_cart'))


def remove_cart_item(request, item_id):
    """ remove_cart_item view is used to remove an item from the users cart """

    product = get_object_or_404(Product, pk=item_id)
    cart = request.session.get('cart', {})

    cart.pop(item_id)
    messages.success(request, f'Removed {product.name} from your cart')

    request.session['cart'] = cart

    return redirect(reverse('view_cart'))

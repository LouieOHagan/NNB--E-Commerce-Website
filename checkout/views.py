from django.shortcuts import render, redirect, reverse
from .forms import OrderForm


def checkout(request):
    """ view_cart view renders the cart page.
    It displays the items in the users cart
    """
    cart = request.session.get('cart', {})
    if not cart:
        return redirect(reverse('display_products'))

    order_form = OrderForm()
    context = {
        'order_form': order_form,
    }

    return render(request, 'checkout/checkout.html', context)

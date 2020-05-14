from django.shortcuts import render


def view_cart(response):
    return render(response, 'cart/cart.html')

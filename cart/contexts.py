from django.conf import settings
from decimal import Decimal
from django.shortcuts import get_object_or_404
from products.models import Product


def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price_current
        product_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery_cost = Decimal(settings.STANDARD_DELIVERY_COST)
        for_free_delivery = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery_cost = 0
        for_free_delivery = 0

    grand_total = delivery_cost + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery_cost': delivery_cost,
        'for_free_delivery': for_free_delivery,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context

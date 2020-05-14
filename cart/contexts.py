from django.conf import settings


def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery_cost = settings.STANDARD_DELIVERY_COST
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

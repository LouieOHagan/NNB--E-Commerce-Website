from django import template


register = template.Library()


@register.filter(name='multiply')
def multiply(price_current, quantity):
    return price_current * quantity

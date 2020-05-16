from django.contrib import admin
from .models import Order, OrderProduct


class OrderProduct(admin.TabularInline):
    model = OrderProduct

    readonly_fields = (
        'product_cost',
    )


class OrderAdmin(admin.ModelAdmin):
    inlines = [
        OrderProduct,
    ]

    readonly_fields = (
                       'order_number',
                       'order_date',
                       'total',
                       'delivery_cost',
                       'grand_total',
    )

    fields = (
              'order_number',
              'order_date',
              'full_name',
              'email_address',
              'street_address1',
              'street_address2',
              'town_or_city',
              'county',
              'postcode',
              'country',
              'total',
              'delivery_cost',
              'grand_total',
    )

    list_display = (
        'order_number',
        'order_date',
        'total',
        'delivery_cost',
        'grand_total',
    )

    ordering = (
        '-order_date',
    )


admin.site.register(Order, OrderAdmin)

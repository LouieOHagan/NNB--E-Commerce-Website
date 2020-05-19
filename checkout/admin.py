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
                       'original_cart',
                       'stripe_pid',
    )

    fieldsets = [
        ('Order Information', {
            'fields': [
                'order_number',
                'order_date',
                'full_name',
                'email_address',
            ]
        }),
        ('Delivery Details', {
            'fields': [
                'street_address1',
                'street_address2',
                'town_or_city',
                'county',
                'postcode',
                'country',
            ]
        }),
        ('Payment Details', {
            'fields': [
                'total',
                'delivery_cost',
                'grand_total',
                'original_cart',
                'stripe_pid',
            ]
        }),
    ]

    list_display = (
        'order_number',
        'order_date',
        'full_name',
        'total',
        'delivery_cost',
        'grand_total',
    )

    ordering = (
        '-order_date',
    )

    search_fields = (
        'order_number',
        'full_name',
        'email_address',
    )

    save_on_top = True


admin.site.register(Order, OrderAdmin)

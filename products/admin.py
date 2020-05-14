from django.contrib import admin
from .models import ProductType, Product


class ProductTypeAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

    fieldsets = [
        ('Basic information', {
            'fields': [
                'name',
                'friendly_name',
                'description'
            ]
        }),
    ]


class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Product Information', {
            'fields': [
                'category',
                'name',
                'product_code',
                'product_description',
            ]
        }),
        ('Pricing', {
            'fields': [
                'price_original',
                'price_current',
            ]
        }),
        ('Stock', {
            'fields': [
                'in_stock',
                'stock',
            ]
        }),
        ('Images', {
            'fields': [
                'image_1',
                'image_2',
                'image_3',
                'image_4',
                'image_5',
            ]
        }),
    ]

    list_display = (
        'product_code',
        'name',
        'category',
        'price_original',
        'price_current',
        'in_stock',
    )


admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(Product, ProductAdmin)

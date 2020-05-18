from django.contrib import admin
from .models import ProductType, Product, ProductReview


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

    search_fields = (
        'name',
        'product_code',
        'product_description',
    )

    list_filter = (
        'category',
        'in_stock'
    )

    save_on_top = True


class ReviewAdmin(admin.ModelAdmin):
    readonly_fields = (
                       'date_posted',
    )

    fieldsets = [
        ('User Information', {
            'fields': [
                'user',
                'display_name',
            ]
        }),
        ('Review Information', {
            'fields': [
                'date_posted',
                'title',
                'product',
                'rating',
                'product_review',
            ]
        }),
    ]

    list_display = (
        'user',
        'title',
        'rating',
        'product',
        'date_posted',
    )

    ordering = (
        '-date_posted',
    )

    search_fields = (
        'user',
        'title',
    )

    list_filter = (
        'product',
    )


admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductReview, ReviewAdmin)

from django.contrib import admin
from .models import ProductType


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


admin.site.register(ProductType, ProductTypeAdmin)

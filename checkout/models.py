from django.db import models
from django.conf import settings
from django.db.models import Sum

import uuid

from products.models import Product


class Order(models.Model):
    order_number = models.CharField(max_length=32, editable=False)
    full_name = models.CharField(max_length=50, blank=False)
    email_address = models.EmailField(max_length=254, blank=False)
    street_address1 = models.CharField(max_length=80, blank=False)
    street_address2 = models.CharField(max_length=80, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=80, blank=True)
    postcode = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=40, blank=False)
    order_date = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10,
                                decimal_places=2,
                                null=False,
                                default=0
                                )
    delivery_cost = models.DecimalField(max_digits=6,
                                        decimal_places=2,
                                        null=False,
                                        default=0
                                        )
    grand_total = models.DecimalField(max_digits=10,
                                      decimal_places=2,
                                      null=False,
                                      default=0
                                      )

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()


class OrderProduct(models.Model):
    order = models.ForeignKey(Order,
                              null=False,
                              blank=False, 
                              on_delete=models.CASCADE,
                              related_name='lineitems')
    product = models.ForeignKey(Product,
                                null=False,
                                blank=False,
                                on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    product_cost = models.DecimalField(max_digits=6,
                                       decimal_places=2,
                                       null=False,
                                       blank=False,
                                       editable=False)

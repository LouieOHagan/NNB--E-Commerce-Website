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
        """ Generate a random, unique order number using UUID """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """ This function is used to update the grand_toal of the order
        every time that a product in the order is added/modified.
        """
        self.total = self.lineitems.aggregate(Sum('product_cost'))['product_cost__sum'] or 0
        if self.total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = settings.STANDARD_DELIVERY_COST
        else:
            self.delivery_cost = 0
        self.grand_total = self.total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """ This function will overwrite the default save method
        to check if the order doesnt have an order number assinged,
        if it doesnt the method will assign it a unique number using UUID
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


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

    def save(self, *args, **kwargs):
        """ This function will overwrite the default save method
        to update the product_cost field by ensuring that the the value
        is the products price multiplied by the quantity of the item
        """
        self.product_cost = self.product.price_current * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Product Code {self.product.product_code} \
            on order {self.order.order_number}'

from django.db import models
from django.contrib.auth.models import User


class ProductType(models.Model):
    name = models.CharField(max_length=60)
    friendly_name = models.CharField(max_length=60, blank=True)
    description = models.CharField(max_length=254, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey('ProductType', null=True,
                                 on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    product_code = models.CharField(max_length=254)
    product_description = models.TextField()

    price_original = models.DecimalField(max_digits=6, decimal_places=2,
                                         blank=True, null=True)
    price_current = models.DecimalField(max_digits=6, decimal_places=2)

    in_stock = models.BooleanField(default=False, null=True)
    stock = models.PositiveIntegerField(default=0, blank=True, null=True)

    image_1 = models.ImageField(default='default.png', blank=True)
    image_2 = models.ImageField(blank=True)
    image_3 = models.ImageField(blank=True)
    image_4 = models.ImageField(blank=True)
    image_5 = models.ImageField(blank=True)

    def __str__(self):
        return self.name


class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=60, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField(blank=False, null=False)
    title = models.CharField(max_length=254)
    product_review = models.TextField(max_length=1024, blank=True)

    def __str__(self):
        return self.title

from django.db import models


class ProductType(models.Model):
    name = models.CharField(max_length=60)
    friendly_name = models.CharField(max_length=60, blank=True)
    description = models.CharField(max_length=254, blank=True)

    def __str__(self):
        return self.name

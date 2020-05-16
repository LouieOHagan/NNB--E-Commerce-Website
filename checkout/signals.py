from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderProduct


@receiver(post_save, sender=OrderProduct)
def update_on_save(sender, instance, created, **kwargs):
    """ Signal to call the update_total method in the models.py
    file that will update the grand_total field when a product
    is added or modified in the admin panel
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrderProduct)
def update_on_delete(sender, instance, **kwargs):
    """ Signal to call the update_total method in the models.py
    file that will update the grand_total field when a product
    is removed in the admin panel
    """
    instance.order.update_total()

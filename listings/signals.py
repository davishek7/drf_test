from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Reservation


@receiver(post_save, sender=Reservation)
def check_date(sender, instance, created, **kwargs):
    if instance.check_in > instance.check_out:
        raise ValueError('Start date must be less than end date')
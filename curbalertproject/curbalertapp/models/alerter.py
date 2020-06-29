from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver


class Alerter(models.Model):
    
    address = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=18, decimal_places=10, null=True)
    longitude = models.DecimalField(max_digits=18, decimal_places=10, null=True)
    can_haul_away = models.BooleanField(null=False, default=True)
    user = models.OneToOneField(User, related_name='alerter', on_delete=models.CASCADE)
    
@receiver(post_save, sender=User)
def create_alerter(sender, instance, created, **kwargs):
    if created:
        Alerter.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_alerter(sender, instance, **kwargs):
    instance.alerter.save()
        
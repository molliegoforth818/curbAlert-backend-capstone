from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
# from .hauldistance import HaulDistance


class Alerter(models.Model):
    
    address = models.CharField( max_length = 50) 
    longitude = models.CharField( max_length = 20)
    latitude = models.CharField( max_length = 20)
    can_haul_away = models.BooleanField(null=True)
    user = models.OneToOneField(User, related_name='alerter', on_delete=models.CASCADE)
    
@receiver(post_save, sender=User)
def create_alerter(sender, instance, created, **kwargs):
    if created:
        Alerter.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_alerter(sender, instance, **kwargs):
    instance.alerter.save()
        
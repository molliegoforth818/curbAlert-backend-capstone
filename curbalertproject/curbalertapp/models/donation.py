from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from .alerter import Alerter
from .size import Size
from .category import Category
from datetime import datetime

class Donation(models.Model):    
    alerter = models.ForeignKey(Alerter, null = False, on_delete = models.CASCADE )
    size = models.ForeignKey(Size, on_delete = models.CASCADE )
    description = models.CharField(null = False, max_length = 255 )
    created_at = models.DateTimeField(auto_now_add= True)   
    expires_on = models.CharField(max_length = 10, null=False)
    needs_haul_away = models.BooleanField(default=False)
    picked_up = models.BooleanField(default=False)
    categories = models.ManyToManyField(Category, through="DonationCategory", through_fields=("donation","category"))
    # image = models.ImageField(upload_to='ecommerceapi_images', null=True) *stretch*
    
    class Meta:
        verbose_name = ("Donation")
        verbose_name_plural = ("Donations")        
    @property
    def is_expired(self):
        return datetime.strptime(self.expires_on, '%Y-%m-%d').date() < datetime.today().date()     #get a string convert it to a datetime and get the date from the datetime 
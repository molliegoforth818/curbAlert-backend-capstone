from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Alerter(models.Model):
    
    address = models.CharField(null = False, max_length = 50) 
    longitude = models.CharField(null = False, max_length = 20)
    latitude = models.CharField(null = False, max_length = 20)
    can_haul_away = models.Boolean(null=False)
    haul_distance = models.Boolean(null=False)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    
    class Meta:
        verbose_name = ("Alerter")
        verbose_name_plural = ("Alerters")        
        
    def __str__(self):
        return f"User ID: {self.user}"
    
    # def get_absolute_url(self):
        # return reverse("customer_detail", kwargs={"pk": self.pk})
        
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class HaulDistance(models.Model):
    
    miles = models.IntegerField(null = True)
    
    class Meta:
        verbose_name = ("Haul Distance")
        verbose_name_plural = ("Haul Distances")        
        
    def __str__(self):
        return f"Name: {self.name}"
    
    # def get_absolute_url(self):
        # return reverse("ProductType_detail", kwargs={"pk": self.pk})
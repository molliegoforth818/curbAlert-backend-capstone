from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Size(models.Model):
    
    title = models.CharField(null = False, max_length = 55)
    
    class Meta:
        verbose_name = ("Size")
        verbose_name_plural = ("Sizes")        
        
    def __str__(self):
        return f"Name: {self.name}"
    
    def get_absolute_url(self):
        return reverse("Size_detail", kwargs={"pk": self.pk})
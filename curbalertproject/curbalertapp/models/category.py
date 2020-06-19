from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    
    title = models.CharField(null = False, max_length = 55)
    
    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")        
        
    def __str__(self):
        return f"Name: {self.name}"
    
    def get_absolute_url(self):
        return reverse("Category_detail", kwargs={"pk": self.pk})
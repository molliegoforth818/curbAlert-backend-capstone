from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    CHOICES = (
        ("housewares","Housewares"),
        ("sporting_goods","Sporting Goods"),
        ("clothes","Clothes"),
        ("furniture", "Furniture"),
        ("miscellaneous", "Miscellaneous"),
    )
    title = models.CharField(null = False, max_length = 55, choices=CHOICES)
    
    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")        
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("Category_detail", kwargs={"pk": self.pk})
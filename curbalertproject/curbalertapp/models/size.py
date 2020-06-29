from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Size(models.Model):
    CHOICES = (
     ('1','Small'),('2','Medium'),('3','Large')   #set choices used in model forms
    )
    title = models.CharField(null = False, max_length = 55, choices=CHOICES)
    
    class Meta:
        verbose_name = ("Size")
        verbose_name_plural = ("Sizes")        
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("Size_detail", kwargs={"pk": self.pk})
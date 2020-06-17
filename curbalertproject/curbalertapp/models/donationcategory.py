from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from .donation import Donation
from .category import Category


class DonationCategory(models.Model):
    
    donation = models.ForeignKey(Donation, on_delete = models.CASCADE )
    category = models.ForeignKey(Category, on_delete = models.CASCADE )
   
    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")        
        
    def __str__(self):
        return f"Name: {self.name}"

    def get_absolute_url(self):
        return reverse("DonationCategory_detail", kwargs={"pk": self.pk})   
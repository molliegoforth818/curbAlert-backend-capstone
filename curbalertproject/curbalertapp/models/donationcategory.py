from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from .donation import Donation
from .category import Category


class DonationCategory(models.Model):
    
    donation = models.ForeignKey(Donation, on_delete = models.CASCADE,related_name='donationcategory' )
    category = models.ForeignKey(Category, on_delete = models.CASCADE, related_name='donationcategory' )
   
    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")        

    def __str__(self):
        return f"{self.category}"

    @property
    def category_title(self):
        category = Category.objects.get(pk=self.category.id)
        return category.title


    def get_absolute_url(self):
        return reverse("DonationCategory_detail", kwargs={"pk": self.pk})   
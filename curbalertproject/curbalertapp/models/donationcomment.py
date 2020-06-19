from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from .donation import Donation
from .alerter import Alerter

class DonationComment(models.Model):
    
    title = models.CharField(null = False, max_length = 55)
    donation = models.ForeignKey(Donation, on_delete = models.CASCADE )
    alerter = models.ForeignKey(Alerter, on_delete = models.CASCADE )


    class Meta:
        verbose_name = ("Donation Comment")
        verbose_name_plural = ("Donation Comments")        
    
    def __str__(self):
        return f"Name: {self.name}"
        
    def get_absolute_url(self):
        return reverse("DonationComment_detail", kwargs={"pk": self.pk})
from safedelete.models import SafeDeleteModel
from safedelete.models import HARD_DELETE_NOCASCADE
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from .alerter import Alerter
from .size import Size
from datetime import datetime
import pytz

class Donation(SafeDeleteModel):
    _safedelete_policy = HARD_DELETE_NOCASCADE

    
    alerter = models.ForeignKey(Alerter, null = False, on_delete = models.CASCADE )
    size = models.ForeignKey(Size, on_delete = models.CASCADE )
    description = models.CharField(null = False, max_length = 255 )
    created_at = models.DateTimeField(auto_now_add= True)
    expires_on = models.DateTimeField()
    needs_haul_away = models.BooleanField(null = True)
    picked_up = models.BooleanField(null=True)
    # image = models.ImageField(upload_to='ecommerceapi_images', null=True) *stretch*
    
    class Meta:
        verbose_name = ("Donation")
        verbose_name_plural = ("Donations")        
    @property
    def is_expired(self):
        utc = pytz.UTC
        return self.expires_on < utc.localize(datetime.now())
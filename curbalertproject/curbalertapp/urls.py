from django.urls import path, include
# from .views import *

path('accounts/', include('django.contrib.auth.urls')),

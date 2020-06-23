from django.urls import path, include
from .views import *

app_name = "curbalertapp"

urlpatterns = [
    path('', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout'),
    path('donations/form/', donation_form, name='donation_form'),
    path('donations/', donation_list, name='donations'),
    path('donations/<int:donation_id>/form/', donation_edit_form, name='donation_edit_form'),



]



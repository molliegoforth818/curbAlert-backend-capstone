from django.urls import path, include
from .views import *

app_name = "curbalertapp"

urlpatterns = [
    path('', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout'),
    path('donation/create/', donation_form, name='donation_form'),
    path('mycurbalerts/', my_curb_alerts, name='my_curb_alerts'),
    path('donation/<int:donation_id>/', donation_details, name='donation'),
    path('donation/detail/<int:donation_id>/', donation_detail_for_map, name='donation_detail_for_map'),
    path('donation/<int:donation_id>/edit/', donation_edit_form, name='donation_edit_form'),
]



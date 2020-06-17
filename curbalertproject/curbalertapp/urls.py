from django.urls import path, include
from .views import * 
from .views import register

app_name = "curbalertapp"

urlpatterns = [
    path('', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login', include('django.contrib.auth.urls'), name='login'),
    path('accounts/register', register, name='register'),
    path('logout/', logout_user, name='logout'),

]


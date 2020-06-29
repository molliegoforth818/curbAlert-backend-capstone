from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from curbalertapp.models import Alerter
from django.forms import ValidationError
import geocoder
from django import forms
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    address = forms.CharField(max_length=255)
    can_haul_away = forms.BooleanField(initial=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'address', 'can_haul_away',)


def __init__(self,*args,**kwargs):
    super(RegisterForm, self).__init__(*args,**kwargs)


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()

            lat_long_from_address = geocoder.osm(form.cleaned_data['address']).json
            
            address = form.cleaned_data['address']
            latitude = lat_long_from_address['lat']
            longitude = lat_long_from_address['lng']
            can_haul_away = form.cleaned_data['can_haul_away']
            
            user.alerter.address = address
            user.alerter.latitude = latitude
            user.alerter.longitude = longitude
            user.alerter.can_haul_away = can_haul_away
            user.save()

            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)

            login(request, user)
            return redirect(reverse('curbalertapp:home'))
    else:
        form = RegisterForm()            
    template = 'registration/register.html'
    context = {
        'form':form
    }

    return render(request, template,context)










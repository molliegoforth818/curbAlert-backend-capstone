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
    can_haul_away = forms.BooleanField(initial=True, required=False, label='Would you like to be available to haul away donations?')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'address', 'can_haul_away',)


def __init__(self,*args,**kwargs):
    super(RegisterForm, self).__init__(*args,**kwargs)


def register(request):
    if request.method == 'POST':              
        form = RegisterForm(request.POST)  #Posting to the register form
        if form.is_valid():
            user = form.save()

            lat_long_from_address = geocoder.osm(form.cleaned_data['address']).json  # geocoder to convert Alerter's address into latitude and longitude for the map 
            
            address = form.cleaned_data['address']
            latitude = lat_long_from_address['lat']
            longitude = lat_long_from_address['lng']
            can_haul_away = form.cleaned_data['can_haul_away']
                                                                        #still not 100% sure on why I had to do it this kind of backwards way but it is the only way i got the creation form to work 
            user.alerter.address = address                          #The one to one field on the model complicated it b/c user and alerter were already joined, so I had to set the variables 
            user.alerter.latitude = latitude                           #to strings because without it they were returning as tuples and throwing errors everywhere 
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
        'form':form                      #this is what I'm sending to the html 
    }

    return render(request, template,context)










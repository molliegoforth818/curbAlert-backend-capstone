from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.forms import ValidationError
from .curbalertapp.models import Alerter
  
  
def register(request):
    if request.method == 'POST':
        form_data = request.POST
        
        try:
            if form_data['password'] != form_data['password_confirmation']:
                raise ValidationError("Password and password confirmation do not match.")
            
            alerter= Alerter() 
            new_user = User.objects.create_user(
                username=form_data['username'],
                password=form_data['password']
            )

            alerter=Alerter.objects.create_alerter(
            address=form_data['address'],
            email=form_data['email'],
            can_haul_away=False,
            user=new_user
            )
            alerter.save()
            
            
            user = authenticate(request, username=form_data['username'], password=form_data['password']

)
            if user is not None:
                login(request, user)
                return redirect(reverse('curbalertapp:home'))
        except Exception as e:
            messages.error(request, f'{type(e)}: {e}')
          
                
    template = 'registration/register.html'
    context = {}

    return render(request, template,context)


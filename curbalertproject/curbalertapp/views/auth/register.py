from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from curbalertapp.models import Alerter
from django.forms import ValidationError 
  
def register(request):
    if request.method == 'POST':
        form_data = request.POST
        
        try:
            if form_data['password'] != form_data['password_confirmation']:
                raise ValidationError("Password and password confirmation do not match.")
            
            new_user = User.objects.create_user(
                username=form_data['username'],
                password=form_data['password']
            )

            new_user.alerter.address=form_data['address'],
            new_user.alerter.address=form_data['address'],
            new_user.alerter.email=form_data['email'],
            new_user.alerter.can_haul_away=False
            new_user.alerter.save()
            
            
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


from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
  
  
def register(request):
    if request.method == 'POST':
        form_data = request.POST
        
        try:
            if form_data['password'] != form_data['password_confirmation']:
                raise ValidationError("Password and password confirmation do not match.")
              
            new_user = User.objects.create_user(
                username=form_data['username'],
                email=form_data['email'],
                password=form_data['password'],
                address=form_data['address'],
                can_haul_away=form_data['can_haul_away'],
                haul_distance=form_data['haul_distance']
            )
            
            user = authenticate(request, username=form_data['username'], email=form_data['email'], 
            password=form_data['password'], address=form_data['address'],can_haul_away=form_data['can_haul_away'],
            haul_distance=form_data['haul_distance']

)
            if user is not None:
                login(request, user)
                return redirect(reverse('curbalertapp:home'))
        except Exception as e:
            messages.error(request, f'{type(e)}: {e}')
          
                

    # libraries = Library.objects.all()
    template = 'registration/register.html'
    # context = {
    #     'libraries': libraries
    # }

    return render(request, template)
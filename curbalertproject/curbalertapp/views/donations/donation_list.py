import sqlite3
from django.shortcuts import render, redirect, reverse
from curbalertapp.models import Donation,Size
from django.contrib.auth.decorators import login_required


@login_required
def donation_list(request):
    if request.method == 'GET':
        all_donations = Donation.objects.all()

        template = 'donation/donation_list.html'
        context = {
            'all_donations': all_donations
        }

        return render(request, template, context)
      
    elif request.method == 'POST':
        form_data = request.POST
        new_donation = Donation.objects.create(
            description = form_data['donation_description'],
            expires_on = form_data['expires_on'],
            needs_haul_away =False,
            picked_up = False,
            alerter_id= request.user.id,
            size_id = form_data['donation_size']
        )        

        return redirect(reverse('curbalertapp:donations'))

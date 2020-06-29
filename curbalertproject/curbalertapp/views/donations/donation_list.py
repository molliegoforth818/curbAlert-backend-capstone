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
    
        

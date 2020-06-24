import sqlite3
from django.shortcuts import render, redirect
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from curbalertapp.models import Donation


def get_donations():
    return Donation.objects.all()

@login_required
def donation_form(request):
    if request.method == 'GET':
        donations=get_donations
        template = 'donation/donation_form.html'
        context = {
            'all_donations': donations
        }

        return render(request, template, context)
    
@login_required
def donation_edit_form(request, donation_id):

    if request.method == 'GET':
        donation = get_donations()

        template = 'donation/donation_form.html'
        context = {
            'donation': donation
        }

        return render(request, template, context)
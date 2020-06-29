import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from curbalertapp.models import Donation


def get_donation(donation_id):
    return Donation.objects.get(pk=donation_id)


@login_required
def donation_detail_for_map(request, donation_id):
    donation = get_donation(donation_id)
    if request.method == 'GET':

        template = 'donation/donation_detail_for_map.html'
        context = {
            'donation': donation
        }

        return render(request, template, context)

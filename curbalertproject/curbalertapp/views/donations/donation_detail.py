import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from curbalertapp.models import Donation


def get_donation(donation_id):
    return Donation.objects.get(pk=donation_id)


@login_required
def donation_details(request, donation_id):
    donation = get_donation(donation_id)
    if request.method == 'GET':

        template = 'donation/donation_details.html'
        context = {
            'donation': donation
        }

        return render(request, template, context)

    if request.method == 'POST':
        form_data = request.POST

        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):

            donation.delete()

            return redirect(reverse('curbalertapp:donations'))

        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):

            donation.expires_on = form_data['expires_on'],
            donation.needs_haul_away =False,
            donation.picked_up = False,
            donation.size_id = form_data['donation_size']

            donation.save()

            return redirect(reverse('curbalertapp:donations'))
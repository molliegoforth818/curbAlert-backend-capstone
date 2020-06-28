import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from curbalertapp.models import Donation, DonationCategory, Alerter
from django import forms

class UpdateDonationPickedUp(forms.ModelForm):
    picked_up = forms.BooleanField(initial=False, required=False)

    class Meta:
        model= Donation
        fields= ('picked_up',)

def get_donation(donation_id):
    return Donation.objects.get(pk=donation_id)


@login_required
def donation_details(request, donation_id):
    donation = get_donation(donation_id)
    user_can_haul_away = Alerter.objects.select_related("user").get(user=request.user).can_haul_away
    enable_edit = False
    if request.method == 'GET':
        if request.user == donation.alerter.user:
            enable_edit = True
        if user_can_haul_away: 
            form= UpdateDonationPickedUp(instance=donation)
        template = 'donation/donation_detail.html'
        context = {
            'donation': donation,
            'enable_edit': enable_edit,
            'user_can_haul_away': user_can_haul_away,
            'form': form
        }

        return render(request, template, context)

    if request.method == 'POST':
        form_data = request.POST

        if (
                "actual_method" in form_data
                and form_data["actual_method"] == "PUT"
            ):
            form = UpdateDonationPickedUp(request.POST, instance=donation)
            if form.is_valid():
                form.save()  
            template = 'donation/donation_detail.html'
            context = {
                'donation': donation,
                'enable_edit': enable_edit,
                'user_can_haul_away': user_can_haul_away,
                'form': form
            }

            return render(request, template, context)
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):

            donation.delete()

            return redirect(reverse('curbalertapp:my_curb_alerts'))


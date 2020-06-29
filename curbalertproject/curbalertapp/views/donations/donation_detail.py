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
    user_can_haul_away = Alerter.objects.select_related("user").get(user=request.user).can_haul_away #if the user that is logged in has agreed to haul away 
    enable_edit = False
    if request.method == 'GET':
        if request.user == donation.alerter.user:
            enable_edit = True                                  #getting donation details 
        if user_can_haul_away: 
            form= UpdateDonationPickedUp(instance=donation)  #instance of the model that the form is expecting 
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
                and form_data["actual_method"] == "PUT"   #put method to change the one field to show that the donation has been picked up 
            ):
            form = UpdateDonationPickedUp(request.POST, instance=donation) #another instance 
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

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from curbalertapp.models import Donation


@login_required
def home(request):
    if request.method == 'GET':
        available_donation_queryset = Donation.objects.select_related("alerter").filter(picked_up=False)
        available_donations = []
        for donation in available_donation_queryset:
            available_donations.append({
                'id':donation.id,'description': donation.description, 'latitude': donation.alerter.latitude, 'longitude': donation.alerter.longitude
            })        
        template = 'home.html'
        context = {
            'available_donations':available_donations
        }
        return render(request, template, context)

# get all donations
# filter down to only donations with alerter ids
#take all of the alerter ids and EITHER make a call to fetch EACH alterer, or filter all the alters to only the ids that you have gathered from donations 
#loop through the alerters and get lat long and make a marker for each 

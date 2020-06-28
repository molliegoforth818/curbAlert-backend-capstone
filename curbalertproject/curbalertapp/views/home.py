from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from curbalertapp.models import Donation, Alerter


@login_required
def home(request):
    if request.method == 'GET':
        available_donation_queryset = Donation.objects.select_related("alerter").filter(picked_up=False)
        available_donations = []
        all_donations = available_donation_queryset
        for donation in available_donation_queryset:
            available_donations.append({
                'id':donation.id,'description': donation.description, 'latitude': donation.alerter.latitude, 'longitude': donation.alerter.longitude, 'is_expired':donation.is_expired, 'user':donation.alerter.user.username, 'needs_haul_away': donation.needs_haul_away, 'can_haul_away': donation.alerter.can_haul_away
            })        
        template = 'home.html'
        context = {
            'available_donations':available_donations,
            'all_donations': all_donations

        }
        return render(request, template, context)

# get all donations
# filter down to only donations with alerter ids
#take all of the alerter ids and EITHER make a call to fetch EACH alterer, or filter all the alters to only the ids that you have gathered from donations 
#loop through the alerters and get lat long and make a marker for each 
#         can_haul_away = False
# user_from_alerter=Alerter.objects.get(user=request.user)
#         can_haul_away = user_from_alerter.can_haul_away
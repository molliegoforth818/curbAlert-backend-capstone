from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from curbalertapp.models import Donation, Alerter


@login_required
def home(request):
    if request.method == 'GET':
        available_donations = []
        user_can_haul_away = Alerter.objects.select_related("user").get(user=request.user).can_haul_away
        donations_that_are_not_mine_and_need_pick_up=Donation.objects.select_related("alerter").exclude(alerter=request.user.id).filter(picked_up=False)
        my_donations = Donation.objects.select_related("alerter").filter(alerter=request.user.id)       
        for donation in donations_that_are_not_mine_and_need_pick_up:
            available_donations.append({
                'id':donation.id,
                'description': donation.description, 
                'latitude': donation.alerter.latitude, 
                'longitude': donation.alerter.longitude, 
                'is_expired':donation.is_expired, 
                'user':donation.alerter.user.username, 
                'needs_haul_away': donation.needs_haul_away, 
            })        
        template = 'home.html'
        context = {
            'my_donations': my_donations,
            'available_donations': available_donations,
            'user_can_haul_away': user_can_haul_away

        }
        return render(request, template, context)

# get all donations
# filter down to only donations with alerter ids
#take all of the alerter ids and EITHER make a call to fetch EACH alterer, or filter all the alters to only the ids that you have gathered from donations 
#loop through the alerters and get lat long and make a marker for each 
#         can_haul_away = False
# user_from_alerter=Alerter.objects.get(user=request.user)
#         can_haul_away = user_from_alerter.can_haul_away
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from curbalertapp.models import Donation, Alerter


@login_required
def home(request):
    if request.method == 'GET':         #getting all donations
        available_donations = []
        user_can_haul_away = Alerter.objects.select_related("user").get(user=request.user).can_haul_away                                                 
        donations_that_are_not_mine_and_need_pick_up=Donation.objects.select_related("alerter").exclude(alerter=request.user.id).filter(picked_up=False)   #getting all donations that aren't the logged in users   
        my_donations = Donation.objects.select_related("alerter").filter(alerter=request.user.id)      #filtering down all of the donations to the specifications I'm looking to display on the home page  
        for donation in donations_that_are_not_mine_and_need_pick_up:                                #relating the name alerter to use some properties on alerter to filter and identify logged in user
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
            'user_can_haul_away': user_can_haul_away     # this is what im sending to html 

        }
        return render(request, template, context)
 

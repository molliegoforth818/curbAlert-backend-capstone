import sqlite3
from django.shortcuts import render, redirect, reverse
from curbalertapp.models import Donation,Size
from django.contrib.auth.decorators import login_required


@login_required
def my_curb_alerts(request):
    if request.method == 'GET':
        
        my_curb_alerts = Donation.objects.filter(alerter=request.user.id)
        active_curb_alerts = []
        expired_curb_alerts = []
        for curb_alert in my_curb_alerts:
            if curb_alert.is_expired:
                expired_curb_alerts.append(curb_alert)
            else:
                active_curb_alerts.append(curb_alert)
        template = 'donation/my_curb_alerts.html'
        context = {
            'active_curb_alerts': active_curb_alerts,
            'expired_curb_alerts': expired_curb_alerts
        }

        return render(request, template, context)

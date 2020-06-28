import sqlite3
from django.shortcuts import render, redirect
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from curbalertapp.models import Donation, Category, DonationCategory, Size
from django import forms


@login_required
def test_donation_edit_form(request, donation_id):
    donation = Donation.objects.get(pk=donation_id)
    context = {
        "donation": donation
    }
    if request.method == 'POST':
        context["method"] = "POST"
    else:
        context['method'] = "GET"
    template = 'donation/test_donation_edit_form.html'
    return render(request, template, context)

import sqlite3
from django.shortcuts import render, redirect
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from curbalertapp.models import Donation, Category, DonationCategory, Size, Alerter
from django import forms
from datetime import datetime

class DonationForm(forms.Form):
    size = forms.ModelChoiceField(queryset=Size.objects.all())
    categories = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Category.objects.all())
    description = forms.CharField(max_length=255)
    expires_on = forms.DateField(widget=forms.SelectDateWidget)

def __init__(self,*args,**kwargs):
    super(DonationForm, self).__init__(*args,**kwargs)


class UpdateDonation(forms.ModelForm):
    size = forms.ModelChoiceField(queryset=Size.objects.all())
    categories = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Category.objects.all())
    description = forms.CharField(max_length=255)
    expires_on = forms.DateField(widget=forms.SelectDateWidget)
    needs_haul_away = forms.BooleanField(initial=False, required=False)

    def __init__(self,*args,**kwargs):
        if kwargs.get('instance'):
            donation_categories = DonationCategory.objects.filter(donation_id=kwargs['instance'].id).select_related('category').all()
            initial = kwargs.setdefault('initial',{})
            initial['categories'] = [donation_category.category for donation_category in donation_categories] 
        forms.ModelForm.__init__(self, *args, **kwargs)

    class Meta:
        model= Donation
        fields= ('size','description','expires_on','needs_haul_away')


    
def get_donations():
    return Donation.objects.all()

@login_required
def donation_form(request):
    if request.method =='POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            alerter = Alerter.objects.get(pk=request.user.id)
            new_donation = Donation.objects.create(
                description = form.cleaned_data['description'],
                expires_on = datetime.strftime(form.cleaned_data['expires_on'], '%Y-%m-%d'),
                needs_haul_away =False,
                picked_up = False,
                alerter= alerter,
                size = form.cleaned_data['size']
            )
            for category in form.cleaned_data['categories']:                
                donation_category = DonationCategory.objects.create(donation=new_donation, category=Category.objects.get(title=category))


                    
        return redirect(reverse('curbalertapp:home')) 
    else:
        form= DonationForm()
        template = 'donation/donation_form.html'
        context = {
            'form': form
        }
        return render(request, template, context)        
    
@login_required
def donation_edit_form(request, donation_id):
    donation = Donation.objects.get(pk=donation_id)
    if request.method == 'POST':
        form = UpdateDonation(request.POST, instance=donation)
        if form.is_valid():
            form.save()
            all_donation_categories = DonationCategory.objects.filter(donation=donation).all()
            for donation_category in all_donation_categories:
                donation_category.delete()
            for category in form.cleaned_data['categories']:
                donation_category, created = DonationCategory.objects.get_or_create(donation=donation, category=category)
            
        return redirect(reverse('curbalertapp:home')) 
    
    else: 
        form = UpdateDonation(instance=donation)
        template = 'donation/donation_edit_form.html'
        context = {
            'form': form,
            "donation": donation,
        }

        return render(request, template, context)


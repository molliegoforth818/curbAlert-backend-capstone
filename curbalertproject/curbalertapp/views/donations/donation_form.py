import sqlite3
from django.shortcuts import render, redirect
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from curbalertapp.models import Donation, Category, DonationCategory, Size
from django import forms

class DonationForm(forms.Form):
    size = forms.ChoiceField(choices=[('1','Small'),('2','Medium'),('3','Large')])
    category = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=[('Housewares', 'Housewares'),('Sporting Goods','Sporting Goods'),('Clothes','Clothes'),('Furniture','Furniture'),('Miscellaneous','Miscellaneous')])
    description = forms.CharField(max_length=255)
    expires_on = forms.DateField(widget=forms.SelectDateWidget)

def __init__(self,*args,**kwargs):
    super(DonationForm, self).__init__(*args,**kwargs)

class UpdateDonation(forms.ModelForm):
    size = forms.ModelMultipleChoiceField(queryset=Size.objects.all())
    category = forms.ModelMultipleChoiceField(queryset=Category.objects.all())
    description = forms.CharField(max_length=255)
    expires_on = forms.DateTimeInput()
    picked_up = forms.BooleanField()
    needs_haul_away = forms.BooleanField()

    def __init__(self,*args,**kwargs):
        if kwargs.get('instance'):
            self.id = kwargs['instance'].id 
            donation_categories = DonationCategory.objects.filter(donation_id=kwargs['instance'].id).select_related('category').all()
            initial = kwargs.setdefault('initial',{})
            initial['category'] = [donation_category.category for donation_category in donation_categories] 
        forms.ModelForm.__init__(self, *args, **kwargs)

    class Meta:
        model= Donation
        widgets= {'id': forms.HiddenInput()}
        fields= ('size','description','expires_on','picked_up','needs_haul_away')


def get_donations():
    return Donation.objects.all()

@login_required
def donation_form(request):
    if request.method =='POST':
        form = DonationForm(request.POST)
        if form.is_valid():
    
            new_donation = Donation.objects.create(
                description = form.cleaned_data['description'],
                expires_on = form.cleaned_data['expires_on'],
                needs_haul_away =False,
                picked_up = False,
                alerter_id= request.user.id,
                size_id = form.cleaned_data['size']
            )
            category_queryset = Category.objects.filter(title__in=form.cleaned_data['category']).all()
            for category in category_queryset:

                DonationCategory.objects.create(
                    donation_id = new_donation.id,
                    category_id = category.id
                ) 
                    
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
    donation_categories = DonationCategory.objects.filter(pk=donation_id).select_related('category').all()
    if request.method == 'POST':
        form = UpdateDonation(request.POST, instance=donation)
        donation.size = Size.objects.get(pk=request.POST['size'])
        if form.is_valid():
             form.save()
            # category_queryset = Category.objects.filter(title__in=form.cleaned_data['category']).all()

            # category_get = Category.objects.get(donation_id)
            # diff_category = category_queryset.difference(category_get)
            # for category in diff_category:
            #     print(category.title) 
    

            # edit_donation = Donation.objects.get(pk=donation_id)
            # edit_donation.description = form.cleaned_data['description'],
            # edit_donation.expires_on = form.cleaned_data['expires_on'],
            # edit_donation.needs_haul_away = form.cleaned_data['needs_haul_away'],
            # edit_donation.picked_up = False,
            # edit_donation.size= Size.objects.get(pk=form.cleaned_data['size'])
            # edit_donation.save()

        return redirect(reverse('curbalertapp:home')) 
    else: 
        form = UpdateDonation(instance=donation)
        template = 'donation/donation_edit_form.html'
        context = {
            'form': form,
            "donation": donation
        }

        return render(request, template, context)



            #from steve's example#
    # def save(self, commit=True):
    #    instance = super().save(self,False)
    #    cat = self.cleaned_data['category']
    #    instance.category = cat[0]
    #    instance.save()
    #    return instance

    #from Steve's Article#
    # class Meta:
    #     model = Donation
    #     fields = ('description', 'expires_on', 'picked_up', 'needs_haul_away')
        


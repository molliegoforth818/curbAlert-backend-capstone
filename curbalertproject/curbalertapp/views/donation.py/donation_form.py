import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from curbalertapp.models import Donation
# from .details import get_donation




@login_required
def donation_form(request):
    if request.method == 'GET':
        template = 'donation/donation_form.html'
        context = {}

        return render(request, template, context)
    
# @login_required
# def book_edit_form(request, book_id):

#     if request.method == 'GET':
#         book = get_book(book_id)
#         libraries = get_libraries()

#         template = 'books/form.html'
#         context = {
#             'book': book,
#             'all_libraries': libraries
#         }

#         return render(request, template, context)
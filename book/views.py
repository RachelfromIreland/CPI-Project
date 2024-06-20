from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def book_party(request):
    return HttpResponse("Welcome to the party booking system")
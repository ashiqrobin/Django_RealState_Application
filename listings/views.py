from django.shortcuts import render
from .models import listing

# Create your views here.

def index(request):
    listings = listing.objects.all()
    context = {'lists':listings}
    return render(request, 'listings/listings.html', context)

def listing(request):
    return render(request, 'listings/listing.html')

def search(request):
    return render(request, 'listings/search.html')
from django.shortcuts import render
from django.http import HttpResponse
from .models import Client, Commande, Produit

def index(request):
    template = 'index.html'
    return render(request,template)

def contact_view(request):
    template = 'subpage.html'
    return render(request,template)

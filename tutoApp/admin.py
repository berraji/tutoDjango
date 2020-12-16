from django.contrib import admin

# Register your models here.

from .models import Produit, Client, Commande

admin.site.site_header = 'tutoApp Django'

admin.site.register(Produit)

admin.site.register(Client)

admin.site.register(Commande)


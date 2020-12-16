from django.db import models

# Create your models here.

class Client(models.Model):
    C_Fname = models.CharField(max_length = 200)
    C_Lname = models.CharField(max_length = 200)

    def __str__(self):
        return self.C_Fname + " " + self.C_Lname

class Produit(models.Model):
    des = models.CharField(max_length = 500)
    desc = models.CharField(max_length = 500)
    prix = models.IntegerField(default = 0)

class Commande(models.Model):
    client = models.ForeignKey(Client, on_delete = models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete = models.CASCADE)

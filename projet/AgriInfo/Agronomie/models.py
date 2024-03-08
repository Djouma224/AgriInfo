from django.db import models
from Compte.models import Utilisateur

class Categorie_culture(models.Model):
    nom_categorie=models.CharField(max_length=50)

    def __str__(self):
        return self.nom_categorie

class Culture(models.Model):
    image=models.ImageField(upload_to='culture')
    nom_culture=models.CharField(max_length=50)
    description_culture=models.TextField()
    categorie_culture=models.ForeignKey(Categorie_culture,on_delete=models.CASCADE)

    def __str__(self):
        return self.nom_culture
    
class Endroit_propice(models.Model):
    culture=models.ManyToManyField(Culture)
    nom_endroit=models.CharField(max_length=50)
    nom_ville=models.CharField(max_length=50)
    description_endroit=models.TextField()
    periode_plantation=models.DateField()
    periode_recolte=models.DateField()

    def __str__(self):
        return self.nom_endroit
    
class Technique_culture(models.Model):
    nom_technique=models.CharField(max_length=50)
    description_technique=models.TextField()
    media=models.FileField()
    categorie_culture=models.ForeignKey(Categorie_culture,on_delete=models.CASCADE)

    def __str__(self):
        return self.nom_technique
    
class Actualite(models.Model):
    auteur=models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    titre=models.CharField(max_length=50)
    media=models.FileField()
    contenu=models.TextField()
    date_pub=models.DateTimeField(auto_now=True)
    valid=models.BooleanField(default=False)

    def __str__(self):
        return self.titre



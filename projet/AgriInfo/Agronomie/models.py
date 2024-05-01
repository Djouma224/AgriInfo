from django.db import models
from AgriInfo.settings import AUTH_USER_MODEL
from django.utils import timezone


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
    
class EndroitPropice(models.Model):
    nom_endroit = models.CharField(max_length=100)  
    ville = models.CharField(max_length=100) 
    desc_endroit = models.TextField()

    def __str__(self):
        return f"{self.nom_endroit} - {self.ville}"
    

class PeriodeDePlantation(models.Model):
    culture = models.ForeignKey(Culture, on_delete=models.CASCADE)  
    endroit = models.ForeignKey(EndroitPropice, on_delete=models.CASCADE)
    date_debut = models.DateField()
    date_fin = models.DateField()

    def __str__(self):
        return f"{self.culture} - {self.endroit} (Du {self.date_debut} au {self.date_fin})"
    
    
class Technique_culture(models.Model):
    nom_technique=models.CharField(max_length=50)
    description_technique=models.TextField()
    video=models.FileField()
    image=models.ImageField(upload_to='technque',blank=True,null=True)
    categorie_culture=models.ForeignKey(Categorie_culture,on_delete=models.CASCADE)

    def __str__(self):
        return self.nom_technique
    
class Actualite(models.Model):
    auteur=models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    titre=models.CharField(max_length=50)
    media=models.FileField()
    contenu=models.TextField()
    date_pub=models.DateTimeField(default=timezone.now)
    valid=models.BooleanField(default=False)

    def __str__(self):
        return self.titre



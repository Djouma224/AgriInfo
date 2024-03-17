from django.db import models

class Materiel_culture(models.Model):
    image=models.ImageField(upload_to='ressource')
    user=models.CharField(max_length=50)
    nom_materiel=models.CharField(max_length=50)
    description_materiel=models.TextField()
    disponibilite=models.BooleanField(default=False)
    prix=models.IntegerField()
    lieu_vente=models.CharField(max_length=50)
    quantite=models.IntegerField()

    def __str__(self):
        return self.nom_materiel
    
class Ressources(models.Model):
    titre_ressource=models.CharField(max_length=50)
    description_ressource=models.TextField()
    media=models.FileField()

    def __str__(self):
        return self.titre_ressource




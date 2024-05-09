from django.db import models
from django.contrib.auth.models import AbstractUser
from Agronomie.models import Actualite
from AgriInfo.settings import AUTH_USER_MODEL

class Notification(models.Model):
    utilisateur = models.ForeignKey(AUTH_USER_MODEL,on_delete=models.CASCADE)
    titre_notif=models.CharField(max_length=150)
    # destinateur=models.ManyToManyField(AUTH_USER_MODEL,related_name="destinateur")
    contenue=models.TextField()
    date_notif=models.DateTimeField(auto_now=True)
    actualite = models.ForeignKey(Actualite,on_delete=models.CASCADE)
    read_notif=models.BooleanField(default=False)

    def __str__(self):
        return self.titre_notif

class Utilisateur(AbstractUser):
    token = models.CharField(max_length=120)
    role=[
        ("agriculteur","agriculteur"),
        ("admin","admin"),
        ("utilisateur","utilisateur")
    ]
    telephone=models.CharField(max_length=15)
    profile=models.ImageField(upload_to="profile",blank=True,null=True)
    roles=models.CharField(max_length=150,choices=role)
    password_confirm=models.CharField(max_length=150)
    notif=models.ManyToManyField(Notification,related_name="notifs",default="")

    def __str__(self):
        return self.username
    
class Commentaire(models.Model):
    auteur=models.ForeignKey(Utilisateur,on_delete=models.CASCADE)
    date_commentaire=models.DateTimeField(auto_now=True)
    contenue=models.TextField()
    actualite=models.ForeignKey(Actualite,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.auteur.username
    

    
    
class Contact(models.Model):
    nom=models.CharField(max_length=150)
    prenom=models.CharField(max_length=150)
    telephone=models.CharField(max_length=15)
    sujet=models.CharField(max_length=150)
    message=models.TextField()

    def __str__(self):
        return self.nom

class Forum(models.Model):
   titre_forum= models.CharField(max_length=150)
   description_forum=models.TextField()
   date_creation=models.DateTimeField(auto_now=True)
   logo=models.ImageField(upload_to="chats",null=True,blank=True)
   user_create=models.ForeignKey(Utilisateur,on_delete=models.CASCADE)

   def __str__(self):
       return self.titre_forum

class Message_forum(models.Model):
    auteur=models.ForeignKey(Utilisateur,on_delete=models.CASCADE)
    contenu_message=models.TextField()
    forum=models.ForeignKey(Forum,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.auteur.username
    


    
    




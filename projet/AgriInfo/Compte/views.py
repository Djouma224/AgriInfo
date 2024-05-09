from django.shortcuts import redirect, render
import secrets

from AgriInfo import settings
from .models import *
from django.core.mail import EmailMessage
from django.contrib.auth import login,logout ,authenticate,update_session_auth_hash
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
import random
# page de contact
def contact(request):
    if request.method =='POST':
        nom=request.POST.get('nom')
        prenom=request.POST.get('prenom')
        tel = request.POST.get('tel')
        sujet = request.POST.get('sujet')
        message = request.POST.get('message')
        new=Contact.objects.create(nom=nom,prenom=prenom,telephone=tel,sujet=sujet,message=message)
        new.save()
    return render(request,'Compte/contact.html')

def inscription(request):
    errors=''
   
 
    if request.method =='POST':
        profil = request.FILES.get('profile_picture')
        username = request.POST.get('username')
        nom_prenom = request.POST.get('nom_prenom')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        role = request.POST.get('role')
        user_exist=Utilisateur.objects.filter(username=username)
        if user_exist:
            errors=f'ce nom utilisateur existe essayer {username}{random.randint(1,999)}'
            return render(request,'Compte/signup.html',{'errors':errors})
        email_exist=Utilisateur.objects.filter(email=email)
        if email_exist:
            errors=f"un utilisateur avec l'email {email} existe deja"
            return render(request,'Compte/signup.html',{'errors':errors})
        if password != password2:
            errors = "vos mots de passes ne sont pas conformes"
            return render(request,'Compte/signup.html',{'errors':errors})
        if len(password) < 4:
            errors = "le mot de passe doit être superieur ou egal à quatre"
            return render(request,'Compte/signup.html',{'errors':errors})
        token = secrets.token_urlsafe(32)
        
        user=Utilisateur.objects.create_user(
            username=username,
            profile=profil,
            email=email,
            telephone=phone,
            roles=role,
            password=password,
            password_confirm=password2,
            last_name=nom_prenom,
            token = token
        )
        user.save()
        return redirect('login')
       

    return render(request,'Compte/signup.html')

def connexion(request):
    errors=''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password =password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            errors = "Mot de passe ou Nom utilisateur incorrecte"
            return render(request,'Compte/login.html',{'errors':errors})
    return render(request,'Compte/login.html')

def deconnexion(request):
    logout(request)
    return redirect('home')

#reinitialisation de mot de passe
def password_reset(request):
    info=""
    errors=""
    if request.method == 'POST':
        email = request.POST.get('email')
        if email=="":
            errors="Veuillez entrer votre mail pour recuper le mot de passe"
            return render(request,'Compte/password_reset.html',{'info':info,'errors':errors})

        user = Utilisateur.objects.filter(email=email)
        if user:
            token = user[0].token
            suject = "Recuperation de mot de passe"
            message = f"cliquer sur ce lien pour reinitialiser votre mot de passe http://127.0.0.1:8000/Compte/password/{token}"
            from_email = settings.EMAIL_HOST_USER
            to_email = email
            email = EmailMessage(suject,message,from_email,[to_email])
            email.send()
            info = f"Un lien vient d'être envoyé dans votre boite Email, merci cliquer pour recuperer votre mot de passe"
            return render(request,'Compte/password_reset.html',{'info':info})
        else:
            errors = f"cet email est incorrect veuilllez ressayer !!!"
            return render(request,'Compte/password_reset.html',{'info':info,'errors':errors})

    return render(request,'Compte/password_reset.html')


def password(request,token):
    info=""
    errors=""
    if request.method == 'POST':
        password = request.POST.get('password')
        user = Utilisateur.objects.filter(token=token)
        users = user[0]
        users.set_password(password)
        users.save()
        errors = f"Votre mot de passe a été modifié avec succès"
        info = f"Entrer votre nouveau mot de passe !!!"
        return render(request,'Compte/login.html',{'errors':errors})
    return render(request,'Compte/password.html',{'info':info})

@login_required(login_url='login')
def change_password(request):
    errors = ""
    info = ""
    user = request.user
    if request.method == 'POST':
        ancien = request.POST.get('password')
        nouveau = request.POST.get('Nouveau_password')
        confirme = request.POST.get('confirmer_passsword')
        if not user.check_password(ancien):
            errors = f"l'ancien mot de passe est incorrect"
            return render(request,'Compte/change_password.html',{'errors':errors})
        if len(nouveau) < 4:
            errors = f"le mot de passe doit avoir au moins 4 caractères"
            return render(request,'Compte/change_password.html',{'errors':errors})
        if nouveau != confirme:
            errors = f"le nouveau mot de passe n'est pas conformes"
            return render(request,'Compte/change_password.html',{'errors':errors})
        user.set_password(nouveau)
        user.save()
        update_session_auth_hash(request,user)
        info = f"Votre mot de passe a été modifié avec succès"
    return render(request,'Compte/change_password.html',{'info':info,"user":user})

@login_required(login_url='login')
def profile(request):
  
    user = request.user
    
    return render(request,'Compte/profil.html',{"user":user})


def modifie_profil(request):
    info = ""
    user = request.user
    # user_profil = Utilisateur.objects.get(user = user)

    if request.method == 'POST':
        # username = request.POST.get('username')
        fullname = request.POST.get('fullName')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        profil = request.FILES.get('profile_picture')
        # new = Utilisateur.objects.update(
        #     # username = username,
        #     last_name = fullname,
        #     email = email,
        #     telephone = phone,
        #     profile = profil
            
        # )
        user.last_name = fullname
        user.email = email
        user.telephone = phone
        image_actuel = user.profile
        if profil:
            user.profile = profil
        else:
            user.profile = image_actuel
        user.save()
        info = f"Mofication effectuée avec succès !!!"
        
        return render(request,'Compte/modifier_profil.html',{'user':user,'info':info})       
    return render(request,'Compte/modifier_profil.html',{'user':user,'info':info})

def voir_commentaires(request,id_actu):
    user = request.user
    actualite = Actualite.objects.prefetch_related('commentaire_set').get(id=id_actu)
    actu = Actualite.objects.get(id=id_actu)
    comments=Commentaire.objects.filter(actualite=actu)
    nb_comment=comments.count()
    if request.method == 'POST':
        contenue = request.POST.get('contenue')
        new = Commentaire.objects.create(
            auteur = user,
            actualite = actu,
            contenue = contenue
        )
        new.save()
        context={'commentaires':actualite,
                'comments':comments,
                'actu':actu,
                'nb_comment':nb_comment}
        return render(request,'Compte/commentaire.html',context)

    context={'commentaires':actualite,
    'comments':comments,
    'nb_comment':nb_comment}
    return render(request,'Compte/commentaire.html',context)

# groupe furums
def forums(request):
    forums=Forum.objects.all()
    context={'forums':forums}
    return render(request,'Compte/forums.html',context)

def forum(request,id_forum):
    forum = Forum.objects.get(id=id_forum)
    messages=Message_forum.objects.filter(forum=forum)
    context={'forum':forum,
             'messages':messages}
    return render(request,'Compte/forum.html',context)


    



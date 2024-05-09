from django.shortcuts import render,get_object_or_404
from .models import *
from Compte.models import *
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request,'Agronomie/index.html')

# def actualite(request):
#     actualite=Actualite.objects.filter(valid=True).order_by('date_pub')
#     context={
#         'actualite':actualite
#     }

    return render(request,'Agronomie/actualites.html',context)
@login_required(login_url="login")
def detail_actualite(request,actu_id):
    user = request.user
    detail = get_object_or_404(Actualite,id=actu_id)
    nb_comment=Commentaire.objects.filter(actualite=detail).count()
    nb_notif = user.notif.filter(read_notif=False).count()
    user_notif = user.notif.filter(read_notif=False).all()
    
    if request.method == 'POST':
        contenue = request.POST.get('contenue')
        new = Commentaire.objects.create(
            auteur = user,
            actualite = detail,
            contenue = contenue,
        )
        new.save()
    user_notif = user.notif.all()
    for users in user_notif:
        if users.actualite == detail:
            users.read_notif = True
            users.save()
            
    
    # notif_id=user.notif.filter(actualite__id=actu_id)
    # print(notif_id)
    # notif_id.read_notif=True
    # user.notif.set()

    nb_notif = user.notif.filter(read_notif=False).count()
    context={'detail':detail,
             'nb_comment':nb_comment,
            'nb_notif':nb_notif }
    return render(request,'Agronomie/actu_detail.html',context)

# detail notifications


#ACtu
def actu(request):
    user_notif=""
    user=request.user
    notification = ""

    if user.is_authenticated:
        nb_notif = user.notif.filter(read_notif=False).count()
        user_notif = user.notif.filter(read_notif=False).all()
    users=Utilisateur.objects.all()
    actualite=Actualite.objects.filter(valid=True).order_by('-date_pub')
    info = ''
    if request.method == 'POST':
        user = request.user
        titre = request.POST.get('titre')
        contenue = request.POST.get('contenue')
        image = request.FILES.get('image')
        new = Actualite.objects.create(
            titre = titre,
            contenu = contenue,
            auteur = user,
            media = image,
            valid = True
        )
        new.save()
        derniere_actu = Actualite.objects.last()

        notifs = Notification.objects.create(
            utilisateur=user,
            titre_notif=titre,
            contenue=contenue,
            actualite = derniere_actu       
        )
        notifs.save()
        for use in users:
            use.notif.add(notifs)
            use.save()
        nb_notif = user.notif.filter(read_notif=False).count()
        user_notif = user.notif.filter(read_notif=False).all()
        
        info = 'Publication effectuée avec succès'
        context={
        'actualite':actualite,
        'info':info,
        'notifs':notifs,
        'user_notif':user_notif,
        'user':user,
        'nb_notif':nb_notif
        }
        return render(request,'Agronomie/actu.html',context)
    if user.is_authenticated:

      context={
        'actualite':actualite,
        'nb_notif':nb_notif,
        'notification':notification,
        'user_notif':user_notif,
        'user':user}
      return render(request,'Agronomie/actu.html',context)
    for i in user_notif:
        print(i.titre_notif)
    notification = Notification.objects.all()
    if user.is_authenticated:
        nb_notif = user.notif.filter(read_notif=False).count()
        user_notif = user.notif.filter(read_notif=False).all()
        context={
            'actualite':actualite,
            'nb_notif':nb_notif,
            'notification':notification,
            'user_notif':user_notif,
            'user':user}
        return render(request,'Agronomie/actu.html',context)
    else:
        context={
            'actualite':actualite,
            'notification':notification,
            'user':user}
        return render(request,'Agronomie/actu.html',context)
    
def culture(request):

    categorie=Categorie_culture.objects.prefetch_related('culture_set').all()
    context={
        'categorie':categorie
    }
    return render(request,'Agronomie/culture.html',context)
"""
def culture(request):
    cultures=Culture.objects.all()
    stock_culture=[item.categorie_culture.nom_categorie for item in cultures]

    context={
      'stock_culture':stock_culture
    }
    return render(request,'Agronomie/culture.html',context)


def culture(request):
    culture_cereal=Culture.objects.filter(categorie_culture__nom_categorie='Céreales')
    culture_legume=Culture.objects.filter(categorie_culture__nom_categorie='Légumes')
    culture_tubercule=Culture.objects.filter(categorie_culture__nom_categorie='Tubercules')
    # categorie_cultures=Categorie_culture.objects.all()
    # for categorie in Categorie_culture.objects.all():
    #     for item in categorie:
    #         pass
    context={
        'culture_cereal':culture_cereal,
        'culture_legume':culture_legume,
        'culture_tubercule':culture_tubercule
    }
    return render(request,'Agronomie/culture.html',context)
"""
def detail_culture(request,my_id):
    detail=get_object_or_404(Culture,id=my_id)
    context={
        'detail':detail
    }

    return render(request,'Agronomie/detail_culture.html',context)

def technique(request):

    technique=Technique_culture.objects.all()
    context={
        'technique':technique
    }
    return render(request,'Agronomie/technique_culture.html',context)

def search_culture(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        culture = Culture.objects.filter(nom_culture__icontains=search) | Culture.objects.filter(categorie_culture__nom_categorie__icontains=search)
        context = {
            'culture':culture
        }
        return render(request,'Agronomie/search_culture.html',context)

# calendrier agricole
def calendrier(request):
    calendriers = PeriodeDePlantation.objects.all()
    villes = EndroitPropice.objects.all()
   
    context={'calendriers':calendriers,
            'villes':villes}
    return render(request,'Agronomie/calendrier.html',context)

def search_calendrier(request):
     if request.method == 'GET':
        localite = request.GET.get('localite')
        culture = request.GET.get('culture')
        ville = request.GET.get('ville')
        search = PeriodeDePlantation.objects.filter(endroit__nom_endroit__icontains=localite) | PeriodeDePlantation.objects.filter(endroit__ville__icontains=ville) | PeriodeDePlantation.objects.filter(culture__nom_culture__icontains=culture)
        context={
            
            'search':search}
        return render(request,'Agronomie/calendrier_search.html',context)

def apropos(request):
    return render(request,'Agronomie/apropos.html')



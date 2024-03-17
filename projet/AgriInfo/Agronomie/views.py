from django.shortcuts import render,get_object_or_404
from .models import *

def home(request):
    return render(request,'Agronomie/index.html')

def actualite(request):
    actualite=Actualite.objects.filter(valid=True)
    context={
        'actualite':actualite
    }

    return render(request,'Agronomie/actualites.html',context)

def detail_actualite(request,actu_id):
    detail = get_object_or_404(Actualite,id=actu_id)
    context={'detail':detail}
    return render(request,'Agronomie/detail_actualite.html',context)


#ACtu
def actu(request):
    actualite=Actualite.objects.filter(valid=True).order_by('-date_pub')
    context={
        'actualite':actualite}
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



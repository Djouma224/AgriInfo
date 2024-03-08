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

from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('actualite',actualite,name='actualite'),
    path('detail_actualite/<int:actu_id>',detail_actualite,name='detail_actualite'),
    path('actu',actu,name='actu')
]
from django.urls import path
from .views import *

urlpatterns = [
    path('contact',contact,name='contact'),
    path('signup',inscription,name='signup'),
    path('login',connexion,name='login'),
    path('logout',deconnexion,name='logout'),
    path('password_reset',password_reset, name='password_reset'),
    path('password/<str:token>',password, name='password'),
    path('profil',profile, name='profil'),
    path('change_password',change_password,name='change_password'),
    path('modifier_profil',modifie_profil, name='modifier_profil'),
    path('voir_commentaires/<int:id_actu>',voir_commentaires, name='voir_commentaires'),

]
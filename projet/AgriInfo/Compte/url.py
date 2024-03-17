from django.urls import path
from .views import *

urlpatterns = [
    path('contact',contact,name='contact'),
    path('signup',inscription,name='signup'),
    path('login',connexion,name='login'),
    path('logout',deconnexion,name='logout'),
    path('password_reset',password_reset, name='password_reset'),
    path('password/<str:token>',password, name='password'),
    path('profile',profile, name='profile'),
]
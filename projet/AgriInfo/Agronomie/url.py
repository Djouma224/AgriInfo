
from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    # path('actualite',actualite,name='actualite'),
    path('detail_actualite/<int:actu_id>',detail_actualite,name='detail_actualite'),
    path('actu',actu,name='actu'),
    path('culture',culture,name="culture"),
    path('detail_culture/<int:my_id>',detail_culture,name='detail_culture'),
      path('technique_culture',technique,name="technique_culture"),
      path('search_culture',search_culture,name="search_culture"),
      path('calendrier',calendrier,name='calendrier'),
      path('search_calendrier',search_calendrier,name="search_calendrier"),
      path('apropos',apropos,name="apropos"),
]
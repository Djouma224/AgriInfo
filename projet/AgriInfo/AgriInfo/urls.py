
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Compte/',include('Compte.url')),
    path('',include('Agronomie.url')),
    path('Ressource',include('Ressource.url')),
    path('accounts/', include('allauth.urls')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from .models import *

class liste(admin.ModelAdmin):
    list_display=('nom','prenom')

admin.site.register(Utilisateur)
admin.site.register(Commentaire)
admin.site.register(Notification)
admin.site.register(Contact,liste)
admin.site.register(Forum)
admin.site.register(Message_forum)



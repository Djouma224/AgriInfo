from django.contrib import admin
from .models import *

admin.site.register(Utilisateur)
admin.site.register(Commentaire)
admin.site.register(Notification)
admin.site.register(Contact)
admin.site.register(Forum)
admin.site.register(Message_forum)




import os

from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter,URLRouter
import Compte.routing
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AgriInfo.settings')

application = ProtocolTypeRouter({
    'http':get_asgi_application(),
    'websocket':AuthMiddlewareStack(
        URLRouter(
            Compte.routing.websocket_urlpatterns
        )
    )
})

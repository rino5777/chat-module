import os

from django.core.asgi import get_asgi_application

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

import my_chat.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Achat.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            my_chat.routing.websocket_urlpatterns
        )
    )
})
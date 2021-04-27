import os

from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

from django.urls import path

from .consumers import WSConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setari.settings')

ws_urlpatterns = [
    path('ws/some_url/', WSConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(URLRouter(ws_urlpatterns))
})

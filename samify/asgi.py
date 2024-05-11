"""
ASGI config for samify project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import authentication.routing  # Assuming your WebSocket routes are defined here

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "samify.settings")

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": AuthMiddlewareStack(
            URLRouter(
                authentication.routing.websocket_urlpatterns  # Your WebSocket URL patterns
            )
        ),
    }
)

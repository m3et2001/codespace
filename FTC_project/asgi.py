"""
ASGI config for FTC_project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
import django 
django.setup()
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter,get_default_application
from django.urls import path
from FTC_users.consumers import *

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FTC_project.settings')

# application = get_asgi_application()

ws_patterns=[

    path('ws/chat/<str:username>/', TestConsumer.as_asgi()),
   path('ws/personal-chat/<slug:second_user>/<slug:first_user>/', PersonalChat.as_asgi())
]

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    'websocket': AuthMiddlewareStack(
    URLRouter(ws_patterns)
    )
})

# application = get_default_application()

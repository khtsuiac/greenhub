# user_db/routing.py
from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/user_db/qr_request', consumers.QRRequestConsumer.as_asgi()),
    path('ws/user_db/qr_verify',consumers.QRVerificationConsumer.as_asgi())
]       
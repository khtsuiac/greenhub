# user_db/routing.py
from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/user_db/qr', consumers.BorrowRequestConsumer.as_asgi()),
]       
from django.urls import path
from .views import chat, ajax


urlpatterns = [
    path('', chat, name='chat'),
    path('ajax/', ajax, name='ajax'),
]
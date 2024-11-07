# myapp/urls.py
from django.urls import path
from .views import ChatMessagesView, ChatView

urlpatterns = [
    path('chat/messages/', ChatMessagesView.as_view(), name='chat_messages'),
    path('chat/', ChatView.as_view(), name='chat_view'),
]

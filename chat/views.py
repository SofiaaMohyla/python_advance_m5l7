from django.shortcuts import render

from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView

from .models import Message  # Приклад моделі для повідомлень


class ChatView(TemplateView):
    template_name = 'chat.html'

class ChatMessagesView(View):
    def get(self, request):
        # Отримання останніх повідомлень
        messages = Message.objects.all().order_by('-timestamp')[:10]
        messages_data = [{"user": msg.user.username, "text": msg.text, "timestamp": msg.timestamp} for msg in messages]
        return JsonResponse({"messages": messages_data})

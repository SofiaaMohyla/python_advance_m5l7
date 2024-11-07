from django.shortcuts import render

from django.http import JsonResponse
from django.views import View

class MyAjaxView(View):
    def get(self, request):
        # Дії для обробки GET-запиту
        data = {"message": "Це відповідь на GET-запит!"}
        return JsonResponse(data)

    def post(self, request):
        # Дії для обробки POST-запиту
        input_data = request.POST.get("data", "")
        response_data = {"message": f"Отримані дані: {input_data}"}
        return JsonResponse(response_data)


def my_template_view(request):
    return render(request, 'index.html')
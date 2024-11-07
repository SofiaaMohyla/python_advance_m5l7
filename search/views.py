# views.py
from django.views import View
from django.views.generic import TemplateView
from django.http import JsonResponse
from .models import Item

class SearchPageView(TemplateView):
    template_name = 'search.html'

class SearchView(View):
    def get(self, request):
        query = request.GET.get('query', '')
        print(query)
        if query:
            results = Item.objects.filter(name__icontains=query)[:10]  # Пошук за ім'ям
            data = [{"id": item.id, "name": item.name} for item in results]
        else:
            data = []

        return JsonResponse({"results": data})

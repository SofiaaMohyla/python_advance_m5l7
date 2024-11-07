# urls.py
from django.urls import path
from .views import SearchPageView, SearchView

urlpatterns = [
    path('search/', SearchPageView.as_view(), name='search_page'),  # Відображення сторінки пошуку
    path('search/results/', SearchView.as_view(), name='search_view'),  # AJAX-запити для пошуку
]

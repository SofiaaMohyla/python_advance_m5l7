from django.urls import path
from .views import MyAjaxView, my_template_view

urlpatterns = [
    path('ajax/', MyAjaxView.as_view(), name='my_ajax_view'),
    path('index/', my_template_view, name='my_ajax_view'),
]

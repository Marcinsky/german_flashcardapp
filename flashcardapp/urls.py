# w flashcardapp/urls.py
from django.urls import path
from .views import lista_fiszek, dodaj_fiszke

urlpatterns = [
    path('lista/', lista_fiszek, name='lista_fiszek'),
    path('dodaj/', dodaj_fiszke, name='dodaj_fiszke'),
]
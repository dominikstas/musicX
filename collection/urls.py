from django.urls import path

from . import views

urlpatterns = [
    path("", views.collection, name="collection"),
    path('dodaj_plyte/', views.dodaj_plyte, name='dodaj_plyte'),

]
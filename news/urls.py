from django.urls import path

from . import views

urlpatterns = [
    path("", views.news, name="news"),
    path('add_preorder/', views.add_preorder, name='add_preorder')
]
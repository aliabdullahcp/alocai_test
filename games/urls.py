from django.urls import path
from . import views

urlpatterns = [
    path('games', views.create, name='game_create'),

]

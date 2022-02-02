from django.urls import path
from . import views

urlpatterns = [
    path('games', views.create, name='game_create'),
    path('best_value_games', views.get_best_value, name='game_best_value'),
]

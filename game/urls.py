"""CMS urls."""
from django.urls import path
from . import views

app_name = 'game'

urlpatterns = [

    path(
        'juego/',
        views.GameView.as_view(),
        name='game'
    ),
    path(
        '',
        views.start_game,
        name='start-game'
    ),
    path(
        'juego/<int:game_id>/',
        views.GameDetailView.as_view(),
        name='game_detail'
    ),

]

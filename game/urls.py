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

]

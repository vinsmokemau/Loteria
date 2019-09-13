from django.db import models


class Game(models.Model):

    class Meta:
        verbose_name = "Juego"
        verbose_name_plural = "Juegos"
    

class Board(models.Model):
    
    game = models.ForeignKey(
        'Game',
        on_delete=models.CASCADE,
    )
    player = models.CharField(
        'jugador',
        max_length=50,
    )

    class Meta:
        verbose_name = "Tablero"
        verbose_name_plural = "Tableros"


class GameCard(models.Model):

    board = models.ForeignKey(
        'Board',
        related_name='cards',
        on_delete=models.CASCADE,
    )
    position = models.IntegerField(
        'posicion',
    )
    card = models.ForeignKey(
        'deck.Card',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "Carta de Juego"
        verbose_name_plural = "Carta de Juegos"

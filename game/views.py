"""Game's Views."""
from .models import (
    Game,
    Board,
    GameCard,
)
from deck.models import Card
from django.views.generic import (
    DetailView,
    TemplateView,
)
from django.http import HttpResponseRedirect


class GameView(TemplateView):

    template_name = "game.html"

    def get_context_data(self, **kwargs):
        context = super(GameView, self).get_context_data(**kwargs)
        context['user_cards'] = Card.objects.order_by('?')[:16]
        context['computer_cards'] = Card.objects.order_by('?')[:16]
        return context


def start_game(request):
    game = Game.objects.create()
    user_board = Board.objects.create(
        game=game,
        player='jugador',
    )
    computer_board = Board.objects.create(
        game=game,
        player='computadora',
    )
    count = 1
    for user_card in Card.objects.order_by('?')[:16]:
        user_game_card = GameCard(
            board=user_board,
            position=count,
            card=user_card,
        )
        user_game_card.save()
        count += 1
    count = 1
    for computer_card in Card.objects.order_by('?')[:16]:
        computer_game_card = GameCard(
            board=computer_board,
            position=count,
            card=computer_card,
        )
        computer_game_card.save()
        count += 1
    return HttpResponseRedirect(game.get_absolute_url())


class GameDetailView(DetailView):

    model = Game
    pk_url_kwarg = "game_id"
    template_name = "game.html"
    context_object_game = "game"

    def get_context_data(self, **kwargs):
        context = super(GameDetailView, self).get_context_data(**kwargs)
        for board in self.object.boards.all():
            if board.player == 'jugador':
                context['player_board'] = board
            else:
                context['computer_board'] = board
        return context

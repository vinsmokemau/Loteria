"""Game's Views."""
import cv2
import pytesseract
from .models import (
    Game,
    Board,
    GameCard,
)
from deck.models import Card
from django.views.generic import (
    DetailView,
)
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404


def start_game(request):
    """Create a new game."""
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
    """Show the boards of two players."""

    model = Game
    pk_url_kwarg = "game_id"
    template_name = "game.html"
    context_object_game = "game"

    def get_context_data(self, **kwargs):
        """Get the context for the view."""
        context = super(GameDetailView, self).get_context_data(**kwargs)
        for board in self.object.boards.all():
            if board.player == 'jugador':
                context['player_board'] = board
            else:
                context['computer_board'] = board
        return context


def new_card(request, game_id):
    """Take a photo of a new card and detect if is in a board."""
    game = get_object_or_404(Game, pk=game_id)
    webcam = cv2.VideoCapture(0)
    check, frame = webcam.read()
    cv2.imwrite(filename='saved_img.jpg', img=frame)
    webcam.release()
    cv2.destroyAllWindows()

    imagen = cv2.imread('saved_img.jpg')

    text = pytesseract.image_to_string(imagen[380:460, 150:480]).lower()
    print(text)
    try:
        card = Card.objects.get(name=text)
        print(card.number)
    except:
        pass

    for board in game.boards.all():
        if text in board.not_checked_cards:
            game_card = GameCard.objects.get(board=board, card__name=text)
            game_card.checked = True
            game_card.save()

    return HttpResponseRedirect(game.get_absolute_url())

from app.domain import Game
from app.domain.data.enums import GameResult, GameState


class GameController:
    """Класс контроллера для Game."""

    def __init__(self, game: Game):
        self._game = game

    def set_game_state(self, state: GameState) -> None:
        self._game.state = state

    def set_game_result(self, game_result: GameResult) -> None:
        self._game.game_result = game_result

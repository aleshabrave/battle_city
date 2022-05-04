from app.controllers.map_controller import MapController
from app.domain import Game
from app.domain.data.enums import GameResult, GameState


class GameController:
    """Класс контроллера для Game."""

    def __init__(self, game: Game, map_controller: MapController):
        self._game = game
        self.map_controller = map_controller

    @property
    def game_state(self) -> GameState:
        return self._game.state

    @property
    def game_result(self) -> GameResult:
        return self._game.game_result

    def update_game_state(self, state: GameState) -> None:
        """Обновить состояние игры."""
        self._game.state = state

    def set_game_result(self, game_result: GameResult) -> None:
        """Установить результат игры."""
        self._game.game_result = game_result

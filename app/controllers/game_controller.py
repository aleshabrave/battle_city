from dataclasses import dataclass

from app.controllers.map_controller import MapController
from app.controllers.observers.lose import LoseObserver
from app.controllers.observers.win import WinObserver
from app.controllers.player_controller import PlayerController
from app.domain.data.enums import GameState
from app.domain.game import Game
from app.domain.interfaces import Observer
from app.domain.map import Map


@dataclass
class GameController:
    """Класс контроллера для Game."""

    game: Game
    player_controller: PlayerController = None
    _map_controller: MapController = None
    _win_observer: Observer = None
    _lose_observer: Observer = None

    def __post_init__(self):
        self.update_controller(init_flag=True)

    def update_controller(self, init_flag=False):
        if not init_flag and not self.game.next_level():
            self.game.state = GameState.FINISHED
            return

        level = self.game.get_current_level()
        self._map_controller = MapController(level.map_)

        player = level.map_.get_entities_by_name("player").pop()
        self.player_controller = PlayerController(player, level.map_)

        castle = level.map_.get_entities_by_name("castle").pop()

        self._lose_observer = LoseObserver(set([player, castle]), self)
        player.add_observer(self._lose_observer)
        castle.add_observer(self._lose_observer)

        enemies = level.map_.get_entities_by_name("enemy")
        if not enemies:
            return

        self._win_observer = WinObserver(enemies, self)

        for enemy in enemies:
            enemy.add_observer(self._win_observer)

    def make_move(self) -> None:
        self._map_controller.update_map()

    def get_current_map(self) -> Map:
        return self.game.get_current_level().map_

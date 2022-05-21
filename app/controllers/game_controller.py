from dataclasses import dataclass
from random import Random

from app.ai.stupid import StupidAI
from app.controllers.map_controller import MapController
from app.controllers.observers.lose import LoseObserver
from app.controllers.observers.win import WinObserver
from app.controllers.player_controller import PlayerController
from app.controllers.tank_controller import TankController
from app.domain.enums import GameState, LevelResult
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
    _ais: list[StupidAI] = None
    _random: Random = Random(1234)

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

        enemies = level.map_.get_entities_by_name("enemy_tank")
        if not enemies:
            return

        self._ais = []
        for enemy in enemies:
            self._ais.append(
                StupidAI(
                    level.map_,
                    TankController(enemy, _cd=2),
                    _seed=Random(self._random.randint(1, 1337)),
                )
            )

        self._win_observer = WinObserver(enemies, self)

        for enemy in enemies:
            enemy.add_observer(self._win_observer)

    def make_move(self) -> None:
        if self.game.get_current_level().state != LevelResult.UNDEFINED:
            return

        self._map_controller.update_map()
        if not self._ais:
            return

        for ai in self._ais:
            ai.make_move()

    def get_current_map(self) -> Map:
        return self.game.get_current_level().map_

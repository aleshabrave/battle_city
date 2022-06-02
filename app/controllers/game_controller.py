import time
from threading import Thread, Event

from app.ai.stupid import StupidAI
from app.controllers.map_controller import MapController
from app.controllers.observers.lose import LoseObserver
from app.controllers.observers.win import WinObserver
from app.controllers.player_controller import PlayerController
from app.controllers.tank_controller import TankController
from app.domain import Level
from app.domain.enums import GameState, LevelState
from app.domain.game import Game
from app.domain.interfaces import Observer
from app.levels.generator import GameGenerator


class GameController(Thread):
    """Класс контроллера для Game."""

    game: Game = None
    player_controller: PlayerController = None
    map_controller: MapController = None

    pause: Event = Event()
    stop: bool = False

    _win_observer: Observer = None
    _lose_observer: Observer = None
    _ais: list[StupidAI] = None

    def __init__(self, timer: float, username: str):
        super(GameController, self).__init__()
        self.timer = timer
        self._username = username

    @staticmethod
    def create(timer: float, username: str, new_game_flag: bool) -> "GameController":
        """Создать контроллер."""
        controller = GameController(timer, username)
        controller.init_game(new_game_flag)
        return controller

    def run(self):
        """Запустить игру."""
        for level in self.game:
            if self.game.state == GameState.FINISHED:
                break

            self._update_inner_controllers(level)

            while level.state == LevelState.UNDEFINED:
                if self.stop:
                    return

                if self.pause.is_set():
                    continue

                self.make_move()
                time.sleep(self.timer)

    def make_move(self) -> None:
        """Сделать ход."""
        self.map_controller.update_map()

        for ai in self._ais:
            ai.make_move()

    def init_game(self, new_game_flag=False) -> None:
        """Инициализировать игру."""
        if not new_game_flag:
            self.game = GameGenerator.load(self._username)

            if self.game is not None:
                return

        self.game = GameGenerator.generate()

    def save(self) -> None:
        """Сохранить игру."""
        GameGenerator.save(self._username, self.game)

    def _update_inner_controllers(self, level: Level) -> None:
        """Обновить внутренние контроллеры."""
        self.map_controller = MapController(level.map_)

        self._update_lose_logic(level)
        self._update_win_logic(level)

    def _update_lose_logic(self, level: Level) -> None:
        """Обновить логику поражения."""
        player = level.map_.get_entities_by_name("player").pop()
        self.player_controller = PlayerController(
            level.map_,
            TankController(player),
        )

        castle = level.map_.get_entities_by_name("castle").pop()

        self._lose_observer = LoseObserver([player, castle], level, self.game)
        player.add_observer(self._lose_observer)
        castle.add_observer(self._lose_observer)

    def _update_win_logic(self, level: Level) -> None:
        """Обновить логику победы."""
        enemies = level.map_.get_entities_by_name("enemy_tank")

        self._ais = []
        for enemy in enemies:
            self._ais.append(
                StupidAI(
                    level.map_,
                    TankController(enemy, _cd=2),
                )
            )

        self._win_observer = WinObserver(enemies, level, self.game)

        for enemy in enemies:
            enemy.add_observer(self._win_observer)

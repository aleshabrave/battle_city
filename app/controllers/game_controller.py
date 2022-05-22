import time
from dataclasses import dataclass
from threading import Thread, Event
from typing import TYPE_CHECKING

from app.ai.stupid import StupidAI
from app.controllers.observers.lose import LoseObserver
from app.controllers.observers.win import WinObserver
from app.domain import Level
from app.domain.enums import LevelResult
from app.domain.game import Game
from app.domain.interfaces import Observer
from app.controllers.map_controller import MapController
from app.controllers.tank_controller import TankController

if TYPE_CHECKING:
    from app.controllers import PlayerController
    from app.levels.generator import GameGenerator


@dataclass
class GameController:
    """Класс контроллера для Game."""

    _timer: float
    _game_generator: "GameGenerator"
    game: Game = None
    player_controller: "PlayerController" = None
    _pause: Event = None
    _game_thread: Thread = None
    _update: Event = None
    _update_thread: Thread = None
    _map_controller: MapController = None
    _win_observer: Observer = None
    _lose_observer: Observer = None
    _ais: list[StupidAI] = None

    def __post_init__(self):
        self._game_thread = Thread(target=self._handle_game, daemon=True)
        self._pause = Event()
        self._update_thread = Thread(target=self._handle_update, daemon=True)
        self._update = Event()

    def start(self) -> None:
        """Запустить игру."""
        self._game_thread.run()

    def unpause(self) -> None:
        """Снять с паузы."""
        self._pause.set()

    def pause(self) -> None:
        """Поставить на паузу."""
        self._pause.clear()

    def _handle_game(self):
        """Обработчик игры."""
        while True:
            self._pause.wait()
            self.make_move()

            if self.game.get_current_level().state != LevelResult.UNDEFINED:
                self._pause.clear()
                self._update.set()

            time.sleep(self._timer)

    def make_move(self) -> None:
        """Сделать ход."""
        self._map_controller.update_map()

        for ai in self._ais:
            ai.make_move()

    def init_game(self, new_game_flag=False) -> None:
        """Инициализировать игру."""
        if not new_game_flag:
            self.game = self._game_generator.load()

            if self.game is not None:
                return

        self.game = self._game_generator.generate()

    def _handle_update(self) -> None:
        """Обработчик внутреннего состояния контроллера."""
        while True:
            self._update.wait()

            if self.game.next_level():
                self._update_inner_controllers()
                self._update_win_logic()
                self._update_lose_logic()

            self._pause.set()
            self._update.clear()

    def save(self) -> None:
        """Сохранить игру."""
        self._game_generator.save(self.game)

    def _update_inner_controllers(self) -> None:
        """Обновить внутренние контроллеры."""
        self._map_controller = MapController(self.get_current_level().map_)

        self._update_lose_logic()
        self._update_win_logic()

    def _update_lose_logic(self) -> None:
        """Обновить логику поражения."""
        player = self.get_current_level().map_.get_entities_by_name("player").pop()
        self.player_controller = PlayerController(
            self.get_current_level().map_,
            TankController(player),
        )

        castle = self.get_current_level().map_.get_entities_by_name("castle").pop()

        self._lose_observer = LoseObserver([player, castle], self)
        player.add_observer(self._lose_observer)
        castle.add_observer(self._lose_observer)

    def _update_win_logic(self) -> None:
        """"Обновить логику победы."""
        enemies = self.get_current_level().map_.get_entities_by_name("enemy_tank")

        self._ais = []
        for enemy in enemies:
            self._ais.append(
                StupidAI(
                    self.get_current_level().map_,
                    TankController(enemy, _cd=2),
                )
            )

        self._win_observer = WinObserver(enemies, self)

        for enemy in enemies:
            enemy.add_observer(self._win_observer)

    def get_current_level(self) -> Level:
        """Получить текущий уровень."""
        return self.game.get_current_level()

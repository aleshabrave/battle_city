from enum import Enum, unique
from typing import Optional

from PyQt5.QtGui import QKeyEvent

from app.controllers.map_controller import MapController
from app.controllers.tank_controller import TankController
from app.domain.data import Direction


@unique
class Key(Enum):
    UP = 16777235
    DOWN = 16777237
    LEFT = 16777234
    RIGHT = 16777236
    SHOOT = 88


class PlayerController:
    def __init__(self, map_controller: MapController):
        self._map_controller = map_controller
        self._player = self._map_controller.map.player
        self._player_tank_controller = TankController(self._player)

    def handle_event(self, event: QKeyEvent) -> None:
        key = self._get_name_of_pressed_key(event)
        if key is None:
            return
        # self._player_tank_controller.update_speed()
        if key == Key.UP:
            self._player_tank_controller.update_direction(Direction.UP)
        elif key == Key.DOWN:
            self._player_tank_controller.update_direction(Direction.DOWN)
        elif key == Key.LEFT:
            self._player_tank_controller.update_direction(Direction.LEFT)
        elif key == Key.RIGHT:
            self._player_tank_controller.update_direction(Direction.RIGHT)
        elif key == Key.SHOOT:
            self._player_tank_controller.fire(self._map_controller.map)
        print(f"FROM UserController: {event.key()}")

    @staticmethod
    def _get_name_of_pressed_key(event: QKeyEvent) -> Optional[Key]:
        key_number = event.key()
        if key_number == Key.UP.value:
            return Key.UP
        elif key_number == Key.DOWN.value:
            return Key.DOWN
        elif key_number == Key.LEFT.value:
            return Key.LEFT
        elif key_number == Key.RIGHT.value:
            return Key.RIGHT
        elif key_number == Key.SHOOT.value:
            return Key.SHOOT
        else:
            return None

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeyEvent

from app.controllers.map_controller import MapController
from app.controllers.tank_controller import TankController
from app.domain.data import Direction
from app.domain.entities.tank import DEFAULT_TANK_SPEED


class PlayerController:
    def __init__(self, map_controller: MapController):
        self._map_controller = map_controller
        self._player_tank_controller = TankController(map_controller.map.player)
        self._init_movement_keys()

    def _init_movement_keys(self):
        self._movement_keys = (Qt.Key_Up, Qt.Key_Down, Qt.Key_Left, Qt.Key_Right)

    def handle_press_key(self, event: QKeyEvent) -> None:
        key = event.key()
        if key == Qt.Key_Up:
            self._player_tank_controller.update_direction(Direction.DOWN)
        elif key == Qt.Key_Down:
            self._player_tank_controller.update_direction(Direction.UP)
        elif key == Qt.Key_Left:
            self._player_tank_controller.update_direction(Direction.LEFT)
        elif key == Qt.Key_Right:
            self._player_tank_controller.update_direction(Direction.RIGHT)
        elif key == Qt.Key_X:
            self._player_tank_controller.fire(self._map_controller.map)
        if key in self._movement_keys:
            self._player_tank_controller.update_speed(DEFAULT_TANK_SPEED)

    def handle_release_key(self, event: QKeyEvent) -> None:
        key = event.key()
        if key in self._movement_keys:
            self._player_tank_controller.update_speed(0)

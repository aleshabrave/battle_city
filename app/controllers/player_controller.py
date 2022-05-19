from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeyEvent

from app.controllers.tank_controller import TankController
from app.domain.data import Direction
from app.domain.entities.tank import DEFAULT_TANK_SPEED, Tank
from app.domain.map import Map


class PlayerController:
    def __init__(self, tank: Tank, map_: Map):
        self._map: Map = map_
        self._tank_controller = TankController(tank)
        self._init_movement_keys()

    def _init_movement_keys(self):
        self._movement_keys = (Qt.Key_Up, Qt.Key_Down, Qt.Key_Left, Qt.Key_Right)

    def handle_press_key(self, event: QKeyEvent) -> None:
        key = event.key()
        if key == Qt.Key_Up:
            self._tank_controller.update_direction(Direction.DOWN)
        elif key == Qt.Key_Down:
            self._tank_controller.update_direction(Direction.UP)
        elif key == Qt.Key_Left:
            self._tank_controller.update_direction(Direction.LEFT)
        elif key == Qt.Key_Right:
            self._tank_controller.update_direction(Direction.RIGHT)
        elif key == Qt.Key_X:
            self._tank_controller.fire(self._map)
        if key in self._movement_keys:
            self._tank_controller.update_speed(DEFAULT_TANK_SPEED)

    def handle_release_key(self, event: QKeyEvent) -> None:
        key = event.key()
        if key in self._movement_keys:
            self._tank_controller.update_speed(0)

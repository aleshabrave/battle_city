from dataclasses import dataclass

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeyEvent

from app.constants import Default
from app.controllers.tank_controller import TankController
from app.domain.enums import Direction
from app.domain.map import Map


@dataclass
class PlayerController:
    """Класс контроллера player."""

    _map: Map
    _tank_controller: TankController

    def __post_init__(self):
        self._init_movement_keys()

    def _init_movement_keys(self):
        self._movement_keys = (Qt.Key_A, Qt.Key_S, Qt.Key_D, Qt.Key_W)

    def handle_press_key(self, event: QKeyEvent) -> None:
        key = event.key()
        if key == Qt.Key_W:
            self._tank_controller.update_direction(Direction.DOWN)
        elif key == Qt.Key_S:
            self._tank_controller.update_direction(Direction.UP)
        elif key == Qt.Key_A:
            self._tank_controller.update_direction(Direction.LEFT)
        elif key == Qt.Key_D:
            self._tank_controller.update_direction(Direction.RIGHT)
        elif key == Qt.Key_X:
            self._tank_controller.fire(self._map)
        if key in self._movement_keys:
            self._tank_controller.update_speed(Default.TANK_SPEED)

    def handle_release_key(self, event: QKeyEvent) -> None:
        key = event.key()
        if key in self._movement_keys:
            self._tank_controller.update_speed(0)

from dataclasses import dataclass

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeyEvent

from app.constants import Default
from app.controllers.tank_controller import TankController
from app.domain.enums import Direction
from app.domain.map import Map


@dataclass
class PlayerController:
    """Controller for player-user."""

    _map: Map
    tank_controller: TankController

    def __post_init__(self):
        self._movement_keys = (Qt.Key_Up, Qt.Key_Down, Qt.Key_Right, Qt.Key_Left)

    def handle_press_key(self, event: QKeyEvent) -> None:
        """Handle press key."""
        key = event.key()
        if key == Qt.Key_Up:
            self.tank_controller.update_direction(Direction.DOWN)
        elif key == Qt.Key_Down:
            self.tank_controller.update_direction(Direction.UP)
        elif key == Qt.Key_Left:
            self.tank_controller.update_direction(Direction.LEFT)
        elif key == Qt.Key_Right:
            self.tank_controller.update_direction(Direction.RIGHT)
        elif key == Qt.Key_Space:
            self.tank_controller.fire(self._map)
        if key in self._movement_keys:
            self.tank_controller.update_speed(Default.TANK_SPEED)

    def handle_release_key(self, event: QKeyEvent) -> None:
        """Handle release key."""
        key = event.key()
        if key in self._movement_keys:
            self.tank_controller.update_speed(0)

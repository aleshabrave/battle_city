from dataclasses import dataclass
from datetime import datetime
from typing import TYPE_CHECKING

from app.constants import Default
from app.domain.enums import Direction

if TYPE_CHECKING:
    from app.domain.entities.tank import Tank
    from app.domain.map import Map


@dataclass
class TankController:
    """Controller for tank"""

    tank: "Tank"
    _cd: int = Default.TANK_CD
    _previous_shot_dttm: datetime = datetime.now()

    def update_speed(self, speed: int) -> None:
        """Update tank speed."""
        self.tank.speed = speed

    def update_direction(self, direction: Direction) -> None:
        """Update tank's direction of travel."""
        self.tank.direction = direction

    def fire(self, map_: "Map") -> None:
        """Fire with cooldown."""
        if (datetime.now() - self._previous_shot_dttm).seconds.real < self._cd:
            return

        self._previous_shot_dttm = datetime.now()
        map_.add_entity(self.tank.get_bullet())

from dataclasses import dataclass
from datetime import datetime
from typing import TYPE_CHECKING

from app.constants import Default
from app.domain.enums import Direction

if TYPE_CHECKING:
    from app.domain.map import Map
    from app.domain.entities.tank import Tank


@dataclass
class TankController:
    """Контроллер для сущности Tank"""

    tank: "Tank"
    _cd: int = Default.TANK_CD
    _previous_shot_dttm: datetime = datetime.now()

    def update_speed(self, speed: int) -> None:
        """Обновить скорость танка."""
        self.tank.speed = speed

    def update_direction(self, direction: Direction) -> None:
        """Обновить направление движения танка."""
        self.tank.direction = direction

    def fire(self, map_: "Map") -> None:
        """Выстрелить."""
        if (datetime.now() - self._previous_shot_dttm).seconds.real < self._cd:
            return

        self._previous_shot_dttm = datetime.now()
        map_.add_entity(self.tank.get_bullet())

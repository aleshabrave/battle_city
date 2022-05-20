from dataclasses import dataclass
from datetime import datetime

from app.domain.data.enums import Direction
from app.domain.entities.tank import Tank
from app.domain.map import Map


@dataclass
class TankController:
    """Контроллер для сущности Tank"""

    _tank: Tank
    _previous_shot_dttm: datetime = datetime.now()
    _cd: int = 1

    def update_speed(self, speed: int) -> None:
        """Обновить скорость танка."""
        self._tank.speed = speed

    def update_direction(self, direction: Direction) -> None:
        """Обновить направление движения танка."""
        self._tank.direction = direction

    def take_damage(self, damage: int) -> None:
        """Принять урон."""
        self._tank.take_damage(damage)

    def fire(self, map_: Map) -> None:
        """Выстрелить."""
        if (datetime.now() - self._previous_shot_dttm).seconds.real < self._cd:
            return

        self._previous_shot_dttm = datetime.now()
        map_.add_entity(self._tank.get_bullet())

    @property
    def tank(self):
        return self._tank

from dataclasses import dataclass
from datetime import datetime
from random import Random

from app.constants import Default
from app.controllers.tank_controller import TankController
from app.domain.enums import Direction
from app.domain.interfaces import Entity
from app.domain.map import Map


@dataclass
class StupidAI:
    """Класс глупого ИИ."""

    _map: Map
    _enemy: TankController
    _cd: int = 500000
    _previous_move_dttm: datetime = datetime.now()

    def make_move(self) -> None:
        if not self._enemy.tank.is_available():
            return

        self._enemy.fire(self._map)

        if (datetime.now() - self._previous_move_dttm).microseconds.real < self._cd:
            return

        player = self._map.get_player()
        castle = self._map.get_entities_by_name("castle").pop()
        new_direction = self.get_new_direction(
            player
            if player.position.dist_to(self._enemy.tank.position)
            > castle.position.dist_to(self._enemy.tank.position)
            else castle
        )

        self._enemy.tank.speed = Default.TANK_SPEED
        self._enemy.update_direction(new_direction)
        self._previous_move_dttm = datetime.now()

    def get_new_direction(self, entity: Entity):
        if (
            entity.position.x
            > self._enemy.tank.position.x + self._enemy.tank.size.width
        ):
            return Direction.RIGHT
        elif entity.position.y + entity.size.height < self._enemy.tank.position.y:
            return Direction.DOWN
        elif entity.position.y > self._enemy.tank.position.y:
            return Direction.UP
        return Direction.LEFT

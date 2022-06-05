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
    _cd: int = 1
    _previous_move_dttm: datetime = datetime.now()

    def make_move(self) -> None:
        """Сходить."""
        if not self._enemy.tank.is_available():
            return

        if (datetime.now() - self._previous_move_dttm).seconds.real < self._cd:
            return

        player = self._map.get_player_tank()
        castle = self._map.get_entities_by_name("castle").pop()
        new_direction = self.get_new_direction(
            player
            if player.position.dist_to(self._enemy.tank.position)
            > castle.position.dist_to(self._enemy.tank.position)
            else castle
        )

        self._enemy.fire(self._map)
        self._enemy.tank.speed = Default.TANK_SPEED
        self._enemy.update_direction(new_direction)
        self._previous_move_dttm = datetime.now()

    def get_new_direction(self, entity: Entity) -> Direction:
        """Получить новое направление."""
        if entity.position.y < self._enemy.tank.position.y:
            return Direction.DOWN
        if entity.position.x < self._enemy.tank.position.x:
            return Direction.LEFT
        if entity.position.y > self._enemy.tank.position.y:
            return Direction.UP
        return Direction.RIGHT

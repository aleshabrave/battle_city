from dataclasses import dataclass
from datetime import datetime
from random import Random

from app.constants import Default
from app.controllers.tank_controller import TankController
from app.domain.enums import Direction
from app.domain.map import Map


@dataclass
class StupidAI:
    """Класс глупого ИИ."""

    _map: Map
    _enemy: TankController
    _seed: Random = Random(1234)
    _cd: int = 2
    _previous_move_dttm: datetime = datetime.now()
    _directions: list[Direction] = None

    def __post_init__(self):
        self._directions = [
            Direction.UP,
            Direction.UP,
            Direction.UP,
            Direction.UP,
            Direction.DOWN,
            Direction.RIGHT,
            Direction.LEFT,
        ]

    def make_move(self) -> None:
        if not self._enemy.tank.is_available():
            return

        self._enemy.fire(self._map)

        if (datetime.now() - self._previous_move_dttm).seconds.real < self._cd:
            return

        next_direction = self._directions[
            self._seed.randint(0, len(self._directions) - 1)
        ]
        self._enemy.tank.speed = Default.TANK_SPEED
        self._cd = self._seed.randint(1, 4)
        self._enemy.update_direction(next_direction)
        self._previous_move_dttm = datetime.now()
        self._seed = Random(self._seed.randint(1, 1337))

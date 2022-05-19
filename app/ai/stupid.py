from dataclasses import dataclass
from datetime import datetime

from app.controllers.tank_controller import TankController
from app.domain.data import Direction
from random import Random

from app.domain.map import Map


@dataclass
class StupidAI:
    """Класс глупого ИИ."""

    _map: Map
    _enemy: TankController
    _seed: Random = Random(1234)
    _cd: int = 1
    _previous_move_datetime: datetime = datetime.now()
    _directions: list[Direction] = None

    def __post_init__(self):
        self._directions = [
            Direction.UP,
            Direction.DOWN,
            Direction.RIGHT,
            Direction.LEFT
        ]

    def make_move(self) -> None:
        if (datetime.now() - self._previous_move_datetime).seconds.real < self._cd:
            return

        next_direction = self._directions[self._seed.randint(0, 3)]
        self._enemy.update_direction(next_direction)
        self._previous_move_datetime = datetime.now()
        self._enemy.fire(self._map)
        self._seed = Random(self._seed.randint(1, 1337))

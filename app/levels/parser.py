import random
from typing import Callable

from app.constants import Default
from app.domain.entities import Block
from app.domain.map import Map
from app.domain.utils import Size, Vector
from app.levels.tank_generator import (
    BigBulletTank,
    DefaultTank,
    FastBulletTank,
    HealthyTank,
    TankFabric,
)


def get_map(filename: str, player_fabric: TankFabric) -> Map:
    """Get map by file."""
    random_fabric = _random_enemy_fabric()

    object_mapper = {
        "P": lambda: player_fabric.get_fabric(enemy_flag=False),
        "W": lambda: _get_block_fabric("default_wall", Default.WALL_HEALTH_POINTS),
        "E": lambda: next(random_fabric).get_fabric(),
        "C": lambda: _get_block_fabric("castle", Default.CASTLE_HEALTH_POINTS),
        ".": lambda: None,
    }

    with open(filename, "r") as file:
        column_counter = 0
        entities = []

        for line in file:
            line = line.replace("\n", "")
            column_counter += 1

            for idx, obj in enumerate(line):
                mapper = object_mapper[obj]
                fabric = mapper()
                if fabric is not None:
                    location = Vector(idx, column_counter) * Default.MAP_CELL_SIZE
                    entity = fabric(location)
                    entities.append(entity)

    return Map(Size((idx + 1), column_counter + 1) * Default.MAP_CELL_SIZE, entities)


def _get_block_fabric(name: str, hps: int) -> Callable:
    """Get block fabric."""

    def fabric(position: Vector) -> Block:
        """Get block."""
        return Block(
            name=name,
            position=position,
            size=Size(1, 1) * Default.MAP_CELL_SIZE,
            health_points=hps,
        )

    return fabric


def _random_enemy_fabric():
    """Get random fabric."""

    rnd = random.Random()
    tank_fabrics = [DefaultTank, FastBulletTank, BigBulletTank, HealthyTank]
    while True:
        yield tank_fabrics[rnd.randint(0, len(tank_fabrics) - 1)]

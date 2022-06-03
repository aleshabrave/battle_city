import random
from typing import Callable

from app.constants import Default
from app.domain.entities import Block, BulletSchema, Tank
from app.domain.enums import Direction
from app.domain.map import Map
from app.domain.utils import Size, Vector
from app.levels.tank_generator import (
    BigBulletTank,
    DefaultTank,
    FastBulletTank,
    HealthyTank,
    TankFabric,
)


def random_enemy_fabric():
    rnd = random.Random()
    tank_fabrics = [DefaultTank, FastBulletTank, BigBulletTank, HealthyTank]
    while True:
        yield tank_fabrics[rnd.randint(0, len(tank_fabrics) - 1)]


def parse_map(filename: str, player_fabric: TankFabric) -> Map:
    """Построить карту по файлу."""
    random_fabric = random_enemy_fabric()

    object_mapper = {
        "P": lambda: player_fabric.get_fabric(enemy_flag=False),
        "W": lambda: _get_block("default_wall", Default.WALL_HEALTH_POINTS),
        "E": lambda: next(random_fabric).get_fabric(),
        "C": lambda: _get_block("castle", Default.CASTLE_HEALTH_POINTS),
        ".": lambda: None,
    }

    with open(filename, "r") as file:
        column_counter = 0
        entities = []

        for line in file:
            line = line.replace("\n", "")
            column_counter += 1

            for idx, obj in enumerate(line):
                mapper = object_mapper[obj]()
                if mapper is not None:
                    location = Vector(idx, column_counter) * Default.MAP_CELL_SIZE
                    entity = mapper(location)
                    entities.append(entity)

    return Map(Size((idx + 1), column_counter + 1) * Default.MAP_CELL_SIZE, entities)


def _get_tank(tank_name: str, bullet_name: str) -> Callable:
    """Получить танк."""
    bullet_schema = BulletSchema(
        name=bullet_name,
        size=Size(1, 1) * (Default.MAP_CELL_SIZE // 4),
        damage=Default.BULLET_DAMAGE,
        speed=Default.TANK_SPEED * 2,
    )

    def wrapper(position: Vector) -> Tank:
        return Tank(
            name=tank_name,
            speed=0,
            direction=Direction.DOWN,
            size=Size(1, 1) * Default.MAP_CELL_SIZE,
            position=position,
            health_points=Default.TANK_HEALTH_POINTS,
            _bullet_schema=bullet_schema,
        )

    return wrapper


def _get_block(name: str, hps: int) -> Callable:
    """Получить блок."""

    def wrapper(position: Vector) -> Block:
        return Block(
            name=name,
            position=position,
            size=Size(1, 1) * Default.MAP_CELL_SIZE,
            health_points=hps,
        )

    return wrapper

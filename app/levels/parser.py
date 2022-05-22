from typing import Callable

from app.domain.entities import Tank, Block
from app.domain.entities.bullet import BulletSchema
from app.domain.enums import Direction
from app.domain.map import Map
from app.constants import Default
from app.domain.utils import Vector, Size


def parse_map(filename: str) -> Map:
    """Построить карту по файлу."""

    with open(filename, "r") as file:
        column_counter = 0
        entities = []

        for line in file:
            line = line.replace("\n", "")
            column_counter += 1

            for idx, obj in enumerate(line):
                mapper = object_mapper[obj]
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


object_mapper = {
    "P": _get_tank("player", "player_bullet"),
    "W": _get_block("default_wall", Default.WALL_HEALTH_POINTS),
    "E": _get_tank("enemy_tank", "enemy_bullet"),
    "C": _get_block("castle", Default.CASTLE_HEALTH_POINTS),
    ".": None,
}

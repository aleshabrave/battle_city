from app.domain.data import Direction, Size, Vector
from app.domain.entities.details import BulletSchema
from app.domain.entities.details.bullet import DEFAULT_DAMAGE
from app.domain.entities.tank import (
    DEFAULT_TANK_HEALTH_POINTS,
    DEFAULT_TANK_SPEED,
    Tank,
)
from app.domain.entities.wall import DEFAULT_WALL_HEALTH_POINTS, Wall
from app.domain.map import CELL_SIZE, Map


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
                    location = Vector(idx, column_counter) * CELL_SIZE
                    entity = mapper(location)
                    entities.append(entity)

    return Map(size=Size((idx + 1), column_counter) * CELL_SIZE, entities=entities)


def _get_default_tank(location: Vector) -> Tank:
    """Создать дефолтный танк."""
    bullet_schema = BulletSchema(
        name="default_bullet",
        size=Size.one() * (CELL_SIZE // 4),
        damage=DEFAULT_DAMAGE,
        speed=DEFAULT_TANK_SPEED * 2,
        location=location,
    )

    return Tank(
        name="default_tank",
        speed=DEFAULT_TANK_SPEED,
        direction=Direction.FORWARD,
        size=Size.one() * CELL_SIZE,
        location=location,
        health_points=DEFAULT_TANK_HEALTH_POINTS,
        bullet_schema=bullet_schema,
    )


def _get_default_wall(location: Vector) -> Wall:
    """Получить дефолтную стену."""

    return Wall(
        name="default_wall",
        location=location,
        size=Size.one() * CELL_SIZE,
        health_points=DEFAULT_WALL_HEALTH_POINTS,
    )


object_mapper = {"W": _get_default_wall, "T": _get_default_tank, ".": None}

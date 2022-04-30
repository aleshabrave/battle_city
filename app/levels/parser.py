from app.domain.data import Size, Vector
from app.domain.entities.details.body import Body
from app.domain.entities.details.bullet import DEFAULT_DAMAGE
from app.domain.entities.details.gun import Gun
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

    gun = Gun(
        name="default_gun",
        location=location,
        size=Size.one() * (CELL_SIZE // 2),
        speed=DEFAULT_TANK_SPEED,
        direction=0,
        bullet_size=Size.one() * (CELL_SIZE // 4),
        bullet_damage=DEFAULT_DAMAGE,
        bullet_speed=DEFAULT_TANK_SPEED * 2,
    )
    body = Body(
        name="default_body",
        location=location,
        size=Size.one() * CELL_SIZE,
        speed=DEFAULT_TANK_SPEED,
        direction=0,
    )

    return Tank(
        name="default_tank",
        gun=gun,
        body=body,
        health_points=DEFAULT_TANK_HEALTH_POINTS,
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

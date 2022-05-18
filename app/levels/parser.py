from app.domain.data import Direction, Size, Vector
from app.domain.entities.bullet import DEFAULT_DAMAGE, BulletSchema
from app.domain.entities.castle import DEFAULT_CASTLE_HEALTH_POINTS, Castle
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

    map_ = Map(Size((idx + 1), column_counter) * CELL_SIZE, {})

    for entity in entities:
        map_.add_entity(entity)

    return map_


def _get_player_tank(location: Vector) -> Tank:
    """Создать танк игрока."""
    bullet_schema = BulletSchema(
        name="player_bullet",
        size=Size(1, 1) * (CELL_SIZE // 4),
        damage=DEFAULT_DAMAGE,
        speed=DEFAULT_TANK_SPEED * 2,
    )

    return Tank(
        name="player",
        speed=0,
        direction=Direction.DOWN,
        size=Size(1, 1) * CELL_SIZE,
        location=location,
        health_points=DEFAULT_TANK_HEALTH_POINTS,
        bullet_schema=bullet_schema,
    )


def _get_enemy_tank(location: Vector) -> Tank:
    """Получить вражеский танк."""
    bullet_schema = BulletSchema(
        name="enemy_bullet",
        size=Size(1, 1) * (CELL_SIZE // 4),
        damage=DEFAULT_DAMAGE,
        speed=DEFAULT_TANK_SPEED * 2,
    )

    return Tank(
        name="enemy_tank",
        speed=DEFAULT_TANK_SPEED,
        direction=Direction.DOWN,
        size=Size(1, 1) * CELL_SIZE,
        location=location,
        health_points=DEFAULT_TANK_HEALTH_POINTS,
        bullet_schema=bullet_schema,
    )


def _get_wall(location: Vector) -> Wall:
    """Получить стену."""

    return Wall(
        name="default_wall",
        location=location,
        size=Size(1, 1) * CELL_SIZE,
        health_points=DEFAULT_WALL_HEALTH_POINTS,
    )


def _get_castle(location: Vector) -> Castle:
    """Получить базу."""

    return Castle(
        name="castle",
        location=location,
        size=Size(1, 1) * CELL_SIZE,
        health_points=DEFAULT_CASTLE_HEALTH_POINTS,
    )


object_mapper = {
    "P": _get_player_tank,
    "W": _get_wall,
    "T": _get_enemy_tank,
    "C": _get_castle,
    ".": None,
}

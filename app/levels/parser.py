from app.domain.data import Direction, Size, Vector
from app.domain.entities.castle import DEFAULT_CASTLE_HEALTH_POINTS, Castle
from app.domain.entities.bullet import DEFAULT_DAMAGE, BulletSchema
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
        player = None

        for line in file:
            line = line.replace("\n", "")
            column_counter += 1

            for idx, obj in enumerate(line):
                mapper = object_mapper[obj]
                if mapper is not None:
                    location = Vector(idx, column_counter) * CELL_SIZE
                    entity = mapper(location)
                    entities.append(entity)
                    if entity.name == "player_tank":
                        if player is not None:
                            raise Exception("Найдено более одного танка игрока")
                        player = entity
        if player is None:
            raise Exception("Танк игрока не найден")

    return Map(Size((idx + 1), column_counter) * CELL_SIZE, entities, player)


def _get_player_tank(location: Vector) -> Tank:
    """Создать танк игрока."""
    bullet_schema = BulletSchema(
        name="player_bullet",
        size=Size(1, 1) * (CELL_SIZE // 4),
        damage=DEFAULT_DAMAGE,
        speed=DEFAULT_TANK_SPEED * 2,
        location=location,
    )

    return Tank(
        name="player_tank",
        speed=0,
        direction=Direction.DOWN,
        size=Size(1, 1) * CELL_SIZE,
        location=location,
        health_points=DEFAULT_TANK_HEALTH_POINTS,
        bullet_schema=bullet_schema,
    )


def _get_enemy_tank(location: Vector) -> Tank:
    """Создать вражеский танк."""
    bullet_schema = BulletSchema(
        name="enemy_bullet",
        size=Size.one() * (CELL_SIZE // 4),
        damage=DEFAULT_DAMAGE,
        speed=DEFAULT_TANK_SPEED * 2,
        location=location,
    )

    return Tank(
        name="enemy_tank",
        speed=DEFAULT_TANK_SPEED,
        direction=Direction.DOWN,
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


def _get_default_castle(location: Vector) -> Castle:
    """Получить дефолтную базу."""

    return Castle(
        name="default_castle",
        location=location,
        size=Size.one() * CELL_SIZE,
        health_points=DEFAULT_CASTLE_HEALTH_POINTS,
    )


object_mapper = {
    "P": _get_player_tank,
    "W": _get_default_wall,
    "T": _get_enemy_tank,
    "C": _get_default_castle,
    ".": None,
}

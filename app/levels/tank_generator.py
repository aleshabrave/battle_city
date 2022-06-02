from typing import Callable

from app.constants import Default
from app.domain.entities import BulletSchema, Tank
from app.domain.enums import Direction
from app.domain.utils import Size, Vector


def _get_tank_fabric(
    bullet_size: int,
    bullet_damage: int,
    bullet_speed: int,
    health_points: int,
    direction: Direction,
    tank_name: str,
    bullet_name: str,
) -> Callable:
    """Получить танк."""

    bullet_schema = BulletSchema(
        name=bullet_name,
        size=Size(1, 1) * bullet_size,
        damage=bullet_damage,
        speed=bullet_speed,
    )

    def wrapper(position: Vector) -> Tank:
        return Tank(
            name=tank_name,
            speed=0,
            direction=direction,
            size=Size(1, 1) * Default.MAP_CELL_SIZE,
            position=position,
            health_points=health_points,
            _bullet_schema=bullet_schema,
        )

    return wrapper


class TankFabric:
    @staticmethod
    def get_fabric(enemy_flag=True):
        """Получить фабрику."""


class DefaultTank(TankFabric):
    @staticmethod
    def get_fabric(enemy_flag=True):
        return _get_tank_fabric(
            bullet_size=Default.MAP_CELL_SIZE // 4,
            bullet_damage=Default.BULLET_DAMAGE,
            bullet_speed=Default.TANK_SPEED * 2,
            health_points=Default.TANK_HEALTH_POINTS,
            direction=Direction.UP if enemy_flag else Direction.DOWN,
            tank_name=f"{'enemy' if enemy_flag else 'player'}_default_tank",
            bullet_name=f"{'enemy' if enemy_flag else 'player'}_bullet",
        )


class BigBulletTank(TankFabric):
    @staticmethod
    def get_fabric(enemy_flag=True):
        return _get_tank_fabric(
            bullet_size=Default.MAP_CELL_SIZE // 2,
            bullet_damage=Default.BULLET_DAMAGE,
            bullet_speed=Default.TANK_SPEED * 2,
            health_points=Default.TANK_HEALTH_POINTS - 1,
            direction=Direction.UP if enemy_flag else Direction.DOWN,
            tank_name=f"{'enemy' if enemy_flag else 'player'}_big_bullet_tank",
            bullet_name=f"{'enemy' if enemy_flag else 'player'}_bullet",
        )


class FastBulletTank(TankFabric):
    @staticmethod
    def get_fabric(enemy_flag=True):
        return _get_tank_fabric(
            bullet_size=Default.MAP_CELL_SIZE // 4,
            bullet_damage=Default.BULLET_DAMAGE,
            bullet_speed=Default.TANK_SPEED * 6,
            health_points=Default.TANK_HEALTH_POINTS - 2,
            direction=Direction.UP if enemy_flag else Direction.DOWN,
            tank_name=f"{'enemy' if enemy_flag else 'player'}_fast_bullet_tank",
            bullet_name=f"{'enemy' if enemy_flag else 'player'}_bullet",
        )


class HealthyTank(TankFabric):
    @staticmethod
    def get_fabric(enemy_flag=True):
        return _get_tank_fabric(
            bullet_size=Default.MAP_CELL_SIZE // 8,
            bullet_damage=Default.BULLET_DAMAGE,
            bullet_speed=Default.TANK_SPEED,
            health_points=Default.TANK_HEALTH_POINTS + 3,
            direction=Direction.UP if enemy_flag else Direction.DOWN,
            tank_name=f"{'enemy' if enemy_flag else 'player'}_healthy_tank",
            bullet_name=f"{'enemy' if enemy_flag else 'player'}_bullet",
        )

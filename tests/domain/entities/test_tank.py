import pytest

from app.domain.data import Vector, Size, Direction
from app.domain.entities import Tank
from app.domain.entities.bullet import BulletSchema

from unittest.mock import MagicMock


class TestsTank:
    def test__init(self):
        name = "test_name"
        location = Vector(54, 54)
        size = Size(1, 1)
        speed = 1
        direction = Direction.DOWN
        health_points = 1
        bullet_schema = BulletSchema("test_bullet", size, 1, speed)

        tank = Tank(name, location, size, speed, direction, health_points, bullet_schema)

        assert tank.name == name
        assert tank.location == location
        assert tank.size == size
        assert tank.speed == speed
        assert tank.direction == direction
        assert tank.health_points == health_points

    def test__get_bullet(self):
        bullet_schema = BulletSchema("test_bullet", Size(1, 2), 3, 4)
        tank_obj = MagicMock(_bullet_schema=bullet_schema)

        bullet = Tank.get_bullet(tank_obj)

        tank_obj._get_bullet_location.assert_called_once_with()
        assert bullet.location == tank_obj._get_bullet_location.return_value
        assert bullet.size == bullet_schema.size
        assert bullet.speed == bullet_schema.speed
        assert bullet.name == bullet_schema.name
        assert bullet.damage == bullet_schema.damage
        assert bullet.direction == tank_obj.direction

    @pytest.mark.parametrize("tank_location,tank_size,direction,expected", [
        (Vector(0, 0), Size(10, 10), Direction.DOWN, Vector(5, -1)),
        (Vector(10, 20), Size(10, 10), Direction.UP, Vector(15, 31)),
        (Vector(20, 10), Size(10, 10), Direction.LEFT, Vector(19, 15)),
        (Vector(40, 50), Size(10, 10), Direction.RIGHT, Vector(51, 55))
    ])
    def test__get_bullet_location(self, tank_location, tank_size, direction, expected):
        tank_obj = MagicMock(direction=direction, location=tank_location, size=tank_size)

        actual = Tank._get_bullet_location(tank_obj)

        assert actual == expected

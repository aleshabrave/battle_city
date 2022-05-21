from unittest.mock import MagicMock, patch

import pytest

from app.domain.entities import Tank
from app.domain.enums import Direction
from app.domain.utils import Size, Vector


class _ModulePatch:
    _PATH = "app.domain.entities.tank"
    BULLET_FACTORY = f"{_PATH}.BulletFactory"


class TestsTank:
    @patch(_ModulePatch.BULLET_FACTORY, new_callable=MagicMock)
    def test__post_init(self, factory):
        tank_obj = MagicMock()

        Tank.__post_init__(tank_obj)

        factory.assert_called_once_with(tank_obj._bullet_schema)
        tank_obj._bullet_factory = factory.return_value

    def test__get_bullet(self):
        bullet_schema = MagicMock()
        tank_obj = MagicMock(_bullet_schema=bullet_schema)

        bullet = Tank.get_bullet(tank_obj)

        tank_obj._get_bullet_position.assert_called_once_with(bullet_schema.size)
        tank_obj._bullet_factory.create.assert_called_once_with(
            position=tank_obj._get_bullet_position.return_value,
            direction=tank_obj.direction,
        )
        assert bullet == tank_obj._bullet_factory.create.return_value

    @pytest.mark.parametrize(
        "tank_location,tank_size,bullet_size,direction,expected",
        [
            (Vector(0, 0), Size(10, 10), Size(2, 2), Direction.DOWN, Vector(4, -3)),
            (Vector(10, 20), Size(10, 10), Size(2, 2), Direction.UP, Vector(14, 31)),
            (Vector(20, 10), Size(10, 10), Size(2, 2), Direction.LEFT, Vector(17, 14)),
            (Vector(40, 50), Size(10, 10), Size(2, 2), Direction.RIGHT, Vector(51, 54)),
        ],
    )
    def test__get_bullet_location(
        self, tank_location, tank_size, bullet_size, direction, expected
    ):
        tank_obj = MagicMock(
            direction=direction, position=tank_location, size=tank_size
        )

        actual = Tank._get_bullet_position(tank_obj, bullet_size)

        assert actual == expected

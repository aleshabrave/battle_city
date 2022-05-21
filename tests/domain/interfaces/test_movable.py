from unittest.mock import MagicMock

import pytest

from app.domain.enums import Direction
from app.domain.interfaces import Movable
from app.domain.utils import Size, Vector


class TestsMovable:
    @pytest.mark.parametrize(
        "speed,direction,expected_shift",
        [
            (1, Direction.RIGHT, Vector(1, 0)),
            (1, Direction.UP, Vector(0, 1)),
            (1, Direction.LEFT, Vector(-1, 0)),
            (1, Direction.DOWN, Vector(0, -1)),
        ],
    )
    def test__update_location(self, speed, direction, expected_shift):
        return
        start_location = Vector(0, 0)
        entity = MagicMock(location=start_location, speed=speed, direction=direction)

        actual_shift = Movable.update_location(
            entity,
        )

        assert entity.location == start_location + actual_shift
        assert actual_shift == expected_shift

    @pytest.mark.parametrize("speed,expected", [(1, True), (-1, True), (0, False)])
    def test__is_moving(self, speed, expected):
        entity = MagicMock(speed=speed)

        actual = Movable.is_moving(entity)

        assert actual == expected

    @pytest.mark.parametrize(
        "position,size,map_size,expected",
        [
            (Vector(4, 0), Size(2, 2), Size(3, 3), Vector(1, 0)),
            (Vector(0, 4), Size(2, 2), Size(3, 3), Vector(0, 1)),
            (Vector(-1, 0), Size(2, 2), Size(2, 2), Vector(0, 0)),
            (Vector(0, -1), Size(2, 2), Size(2, 2), Vector(0, 0)),
            (Vector(-1, -1), Size(2, 2), Size(2, 2), Vector(0, 0)),
        ],
    )
    def test__resolve_out_of_bounds(self, position, size, map_size, expected):
        actual = Movable._resolve_out_of_bounds(position, size, map_size)

        assert actual == expected

    @pytest.mark.parametrize(
        "direction, speed, expected",
        [
            (Direction.UP, 1, Vector(0, 1)),
            (Direction.DOWN, 1, Vector(0, -1)),
            (Direction.RIGHT, 1, Vector(1, 0)),
            (Direction.LEFT, 1, Vector(-1, 0)),
        ],
    )
    def test__get_new_position(self, direction, speed, expected):
        entity_obj = MagicMock(direction=direction, speed=speed)

        actual = Movable._get_new_position(entity_obj)

        assert actual == entity_obj.position + expected

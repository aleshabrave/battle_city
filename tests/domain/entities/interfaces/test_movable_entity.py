from unittest.mock import MagicMock

import pytest

from app.domain.data import Size, Vector, Direction

from app.domain.entities.interfaces import MovableEntity


def test__init():
    name = "test_name"
    location = Vector(0, 0)
    size = Size(1, 1)
    speed = 1
    direction = Direction.UP

    entity = MovableEntity(name, location, size, speed, direction)

    assert entity.name == name
    assert entity.size == size
    assert entity.location == location
    assert entity.speed == speed
    assert entity.direction == direction


@pytest.mark.parametrize(
    "speed,direction,expected_shift",
    [
        (1, Direction.RIGHT, Vector(1, 0)),
        (1, Direction.UP, Vector(0, 1)),
        (1, Direction.LEFT, Vector(-1, 0)),
        (1, Direction.DOWN, Vector(0, -1)),
    ],
)
def test__update_location(speed, direction, expected_shift):
    start_location = Vector(0, 0)
    entity = MagicMock(location=start_location, speed=speed, direction=direction)

    actual_shift = MovableEntity.update_location(entity)

    assert entity.location == start_location + actual_shift
    assert actual_shift == expected_shift


@pytest.mark.parametrize("speed, expected", [(1, True), (-1, True), (0, False)])
def test__is_moving(speed, expected):
    entity = MagicMock(speed=speed)

    actual = MovableEntity.is_moving(entity)

    assert actual == expected

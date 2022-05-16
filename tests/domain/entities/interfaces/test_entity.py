from unittest.mock import MagicMock

import pytest

from app.domain.data.params import Size, Vector
from app.domain.entities.interfaces import Entity


class TestsEntity:
    def test__init(self):
        name = "test_name"
        location = Vector(0, 0)
        size = Size(1, 1)

        entity = Entity(name, location, size)

        assert entity.name == name
        assert entity.size == size
        assert entity.location == location

    def test__move(self):
        start_location = Vector(0, 0)
        shift = Vector(1, 1)
        entity = Entity(name=MagicMock(), location=start_location, size=MagicMock())

        entity.move(shift)

        assert entity.location == start_location + shift

    @pytest.mark.parametrize(
        "entity1,entity2,expected",
        [
            (
                Entity("", Vector(1, 1), Size(1, 1)),
                Entity("", Vector(3, 2), Size(1, 1)),
                False,
            ),
            (
                Entity("", Vector(1, 1), Size(3, 3)),
                Entity("", Vector(3, 2), Size(1, 1)),
                True,
            ),
            (
                Entity("", Vector(1, 1), Size(2, 2)),
                Entity("", Vector(2, 1), Size(2, 2)),
                True,
            ),
            (
                Entity("", Vector(1, 1), Size(2, 2)),
                Entity("", Vector(1, 1), Size(2, 2)),
                True,
            ),
            (
                Entity("", Vector(1, 2), Size(1, 1)),
                Entity("", Vector(3, 1), Size(1, 1)),
                False,
            ),
            (
                Entity("", Vector(1, 1), Size(1, 2)),
                Entity("", Vector(1, 4), Size(1, 2)),
                False,
            ),
        ],
    )
    def test__are_intersected(self, entity1, entity2, expected):
        actual = Entity.are_intersected(entity1, entity2)

        assert actual == expected

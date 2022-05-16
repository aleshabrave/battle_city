from app.domain.data import Vector, Size
from app.domain.entities import Castle


class TestsCastle:
    def test__init(self):
        name = "test_name"
        location = Vector(54, 54)
        size = Size(1, 1)
        health_points = 1

        castle = Castle(name, location, size, health_points)

        assert castle.name == name
        assert castle.location == location
        assert castle.size == size
        assert castle.health_points == health_points

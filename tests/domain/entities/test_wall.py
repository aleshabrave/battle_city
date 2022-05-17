from app.domain.data import Size, Vector
from app.domain.entities import Wall


class TestsWall:
    def test__init(self):
        name = "test_name"
        location = Vector(54, 54)
        size = Size(1, 1)
        health_points = 1

        wall = Wall(name, location, size, health_points)

        assert wall.name == name
        assert wall.location == location
        assert wall.size == size
        assert wall.health_points == health_points

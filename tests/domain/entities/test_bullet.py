from app.domain.data import Direction, Size, Vector
from app.domain.entities import Bullet


class TestsBullet:
    def test__init(self):
        name = "test_name"
        location = Vector(54, 54)
        size = Size(1, 1)
        speed = 1
        direction = Direction.DOWN
        damage = 1

        bullet = Bullet(name, location, size, damage, speed, direction)

        assert bullet.name == name
        assert bullet.location == location
        assert bullet.size == size
        assert bullet.damage == damage
        assert bullet.speed == speed
        assert bullet.direction == direction

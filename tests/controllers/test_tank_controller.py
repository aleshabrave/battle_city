from unittest.mock import MagicMock

import pytest

from app.controllers.tank_controller import TankController
from app.domain.data import Direction


class TestsTankController:
    @pytest.mark.parametrize("new_speed", [54, 108])
    def test__update_speed(self, new_speed):
        controller = TankController(_tank=MagicMock(speed=0))

        controller.update_speed(new_speed)

        assert controller._tank.speed == new_speed

    @pytest.mark.parametrize("new_direction", [Direction.UP, Direction.LEFT])
    def test__update_direction(self, new_direction):
        controller = TankController(_tank=MagicMock(direction=Direction.DOWN))

        controller.update_direction(new_direction)

        assert controller._tank.direction == new_direction

    def test__take_damage(self):
        damage = 54
        controller = TankController(_tank=MagicMock())

        controller.take_damage(damage)

        controller._tank.take_damage.assert_called_once_with(damage)

    def test__fire(self):
        map_ = MagicMock()
        controller = TankController(_tank=MagicMock())

        controller.fire(map_)

        controller._tank.get_bullet.assert_called_once_with()
        map_.add_entity.assert_called_once_with(
            controller._tank.get_bullet.return_value
        )

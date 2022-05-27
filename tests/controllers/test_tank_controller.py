from unittest.mock import MagicMock

import pytest

from app.controllers.tank_controller import TankController
from app.domain.enums import Direction


class TestsTankController:
    @pytest.mark.parametrize("new_speed", [54, 108])
    def test__update_speed(self, new_speed):
        controller = TankController(tank=MagicMock(speed=0))

        controller.update_speed(new_speed)

        assert controller.tank.speed == new_speed

    @pytest.mark.parametrize("new_direction", [Direction.UP, Direction.LEFT])
    def test__update_direction(self, new_direction):
        controller = TankController(tank=MagicMock(direction=Direction.DOWN))

        controller.update_direction(new_direction)

        assert controller.tank.direction == new_direction

    @pytest.mark.parametrize("cd,can_fire", [(0, True), (1, False)])
    def test__fire(self, cd, can_fire):
        map_ = MagicMock()
        controller = TankController(tank=MagicMock(), _cd=cd)

        controller.fire(map_)

        if can_fire:
            controller.tank.get_bullet.assert_called_once_with()
            map_.add_entity.assert_called_once_with(
                controller.tank.get_bullet.return_value
            )
        else:
            assert not controller.tank.get_bullet.called

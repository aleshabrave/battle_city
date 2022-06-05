from unittest.mock import MagicMock

import pytest
from PyQt5.QtCore import Qt

from app.constants import Default
from app.controllers.player_controller import PlayerController
from app.domain.enums import Direction


class TestsPlayerController:
    @pytest.mark.parametrize(
        "key,new_direction",
        [
            (Qt.Key_Left, Direction.LEFT),
            (Qt.Key_Right, Direction.RIGHT),
            (Qt.Key_Down, Direction.UP),
            (Qt.Key_Up, Direction.DOWN),
        ],
    )
    def test__handle_press_key_if_move(self, key, new_direction):
        tank_controller = MagicMock()
        event = MagicMock(key=MagicMock(return_value=key))
        player_controller = PlayerController(MagicMock(), tank_controller)

        player_controller.handle_press_key(event)

        tank_controller.update_direction.assert_called_once_with(new_direction)
        tank_controller.update_speed.assert_called_once_with(Default.TANK_SPEED)

    def test__handle_press_key_if_fire(self):
        map_ = MagicMock()
        tank_controller = MagicMock()
        event = MagicMock(key=MagicMock(return_value=Qt.Key_Space))
        player_controller = PlayerController(map_, tank_controller)

        player_controller.handle_press_key(event)

        tank_controller.fire.assert_called_once_with(map_)
        assert not tank_controller.update_direction.called
        assert not tank_controller.update_speed.called

    @pytest.mark.parametrize("key", [Qt.Key_Left, Qt.Key_Right, Qt.Key_Down, Qt.Key_Up])
    def test__handler_release_key(self, key):
        tank_controller = MagicMock()
        event = MagicMock(key=MagicMock(return_value=key))
        player_controller = PlayerController(MagicMock(), tank_controller)

        player_controller.handle_release_key(event)

        tank_controller.update_speed.assert_called_once_with(0)

from unittest.mock import MagicMock

import pytest

from app.domain.interfaces import Dangerous


class TestsDangerous:
    @pytest.mark.parametrize("damage", [-1, 0])
    def test__post_init_with_exception(self, damage):
        with pytest.raises(ValueError):
            Dangerous(damage=damage)

    def test__do_damage(self):
        living_obj = MagicMock()
        dangerous_obj = Dangerous(damage=1)

        dangerous_obj.do_damage(living_obj)

        living_obj.take_damage.assert_called_once_with(dangerous_obj.damage)

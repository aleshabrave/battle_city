from unittest.mock import MagicMock

import pytest

from app.domain.entities.interfaces import Dangerous


class TestsDangerous:
    def test__init(self):
        damage = 1

        dangerous_obj = Dangerous(damage=damage)

        assert dangerous_obj.damage == damage

    @pytest.mark.parametrize("damage", [-1, 0])
    def test__init_with_exception(self, damage):
        with pytest.raises(ValueError):
            Dangerous(damage=damage)

    def test__do_damage(self):
        """Тест метода do_damage."""
        living_obj = MagicMock()
        dangerous_obj = Dangerous(damage=1)

        dangerous_obj.do_damage(living_obj)

        living_obj.take_damage.assert_called_once_with(dangerous_obj.damage)

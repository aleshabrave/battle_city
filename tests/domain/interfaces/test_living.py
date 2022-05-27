from unittest.mock import MagicMock

import pytest

from app.domain.interfaces import Living


class TestsLiving:
    @pytest.mark.parametrize("health_points", [-1, 0])
    def test__post_init(self, health_points):
        with pytest.raises(ValueError):
            Living(health_points=health_points)

    @pytest.mark.parametrize(
        "health_points,expected", [(1, True), (0, False), (-1, False)]
    )
    def test__is_available(self, health_points, expected):
        living_obj = MagicMock(health_points=health_points)

        actual = Living.is_available(living_obj)

        assert actual == expected

    @pytest.mark.parametrize(
        "health_points,damage,expected",
        [(1, 2, 0), (1, 1, 0), (2, 1, 1)],
    )
    def test__take_damage(self, health_points, damage, expected):
        living_obj = MagicMock(health_points=health_points)

        Living.take_damage(living_obj, damage)

        living_obj.notify.assert_called_once_with()
        assert living_obj.health_points == expected

    @pytest.mark.parametrize("damage", [-1, 0])
    def test__take_damage_with_exception(self, damage):
        with pytest.raises(ValueError):
            Living.take_damage(self=MagicMock(), damage=damage)

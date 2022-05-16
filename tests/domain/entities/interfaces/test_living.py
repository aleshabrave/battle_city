import pytest

from unittest.mock import MagicMock

from app.domain.entities.interfaces import Living


class TestsLiving:
    def test__init(self):
        health_points = 1

        living_obj = Living(health_points=health_points)

        assert living_obj.health_points == health_points

    @pytest.mark.parametrize("health_points", [-1, 0])
    def test__init_with_exception(self, health_points):
        with pytest.raises(ValueError):
            Living(health_points=health_points)

    @pytest.mark.parametrize(
        "health_points,expected", [(1, True), (0, False), (-1, False)]
    )
    def test__is_available(self, health_points, expected):
        living_obj = MagicMock(health_points=health_points)

        result = Living.is_available(living_obj)

        assert result == expected

    @pytest.mark.parametrize(
        "start_health_points,damage,result_health_points",
        [(1, 2, 0), (1, 1, 0), (2, 1, 1)],
    )
    def test__take_damage(self, start_health_points, damage, result_health_points):
        living_obj = Living(health_points=start_health_points)

        living_obj.take_damage(damage)

        assert living_obj.health_points == result_health_points

    @pytest.mark.parametrize("damage", [-1, 0])
    def test__take_damage_with_exception(self, damage):
        with pytest.raises(ValueError):
            Living.take_damage(self=MagicMock(), damage=damage)

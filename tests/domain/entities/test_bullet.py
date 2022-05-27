from unittest.mock import MagicMock, call, patch

import pytest

from app.domain.entities.bullet import Bullet, BulletFactory
from app.domain.interfaces import Living


class _ModulePatch:
    _PATH = "app.domain.entities.bullet"
    MOVABLE = f"{_PATH}.Movable"


class TestsBullet:
    @patch(_ModulePatch.MOVABLE, new_callable=MagicMock)
    def test__update_location_if_no_entity_to_damage(self, movable):
        map_ = MagicMock()
        bullet_obj = MagicMock()
        movable.update_location.return_value = None

        Bullet.update_location(bullet_obj, map_)

        movable.update_location.assert_called_once_with(
            bullet_obj, map_=map_, out_of_bound_remove_flag=True
        )

    @pytest.mark.parametrize("is_available", [False, True])
    @patch(_ModulePatch.MOVABLE, new_callable=MagicMock)
    def test__update_location_if_some_entity_to_damage(self, movable, is_available):
        map_ = MagicMock()
        bullet_obj = MagicMock()
        entity = MagicMock(
            is_available=MagicMock(return_value=is_available), spec=Living
        )
        movable.update_location.return_value = entity

        Bullet.update_location(bullet_obj, map_)

        movable.update_location.assert_called_once_with(
            bullet_obj, map_=map_, out_of_bound_remove_flag=True
        )
        bullet_obj.do_damage.assert_called_once_with(entity)
        if is_available:
            map_.remove_entity.assert_called_once_with(bullet_obj)
        else:
            map_.remove_entity.assert_has_calls([call(entity), call(bullet_obj)])

    @patch(_ModulePatch.MOVABLE, new_callable=MagicMock)
    def test__update_location_if_some_entity_is_other_bullet(self, movable):
        map_ = MagicMock()
        bullet_obj = MagicMock()
        entity = MagicMock(spec=Bullet)
        movable.update_location.return_value = entity

        Bullet.update_location(bullet_obj, map_)

        movable.update_location.assert_called_once_with(
            bullet_obj, map_=map_, out_of_bound_remove_flag=True
        )
        map_.remove_entity.assert_has_calls([call(entity), call(bullet_obj)])


class TestsBulletFactory:
    def test__create(self):
        bullet_schema = MagicMock(damage=1)
        position = MagicMock()
        direction = MagicMock()
        factory = BulletFactory(bullet_schema)

        bullet = factory.create(position, direction)

        assert bullet.name == bullet_schema.name
        assert bullet.position == position
        assert bullet.direction == direction
        assert bullet.size == bullet_schema.size
        assert bullet.damage == bullet_schema.damage
        assert bullet.speed == bullet_schema.speed

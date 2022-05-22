from unittest.mock import MagicMock

import pytest

from app.domain.game import Game


class TestsGame:
    def test__get_current_level(self):
        levels = [MagicMock()]
        game = Game(levels)

        level = game.get_current_level()

        assert level == levels[0]

    def test__get_current_level_idempotency(self):
        levels = [MagicMock()]
        game = Game(levels)

        level1 = game.get_current_level()
        level2 = game.get_current_level()

        assert level1 == level2
        assert level1 == levels[0]

    def test__get_current_level_with_exception(self):
        game = Game([])

        with pytest.raises(IndexError):
            game.get_current_level()

    @pytest.mark.parametrize("count,expected", [(1, [True]), (3, [True, True, False])])
    def test__next_level(self, count, expected):
        levels = [MagicMock(), MagicMock()]
        game = Game(levels)
        actual = []

        for i in range(count):
            actual.append(game.next_level())

        assert actual == expected
        assert game._current_level_index == count - expected.count(False) - 1

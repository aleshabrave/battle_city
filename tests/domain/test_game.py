from unittest.mock import MagicMock

from app.domain.game import Game


class TestsGame:
    def test__iter(self):
        levels = [MagicMock(), MagicMock(), MagicMock()]
        game = Game(levels)

        actual_levels = [level for level in game]

        assert actual_levels == levels

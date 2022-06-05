from unittest.mock import MagicMock, patch

import pytest

from app.db.storage import GameStorage


class _ModulePatch:
    _PATH = "app.db.storage"

    GAME_MODEL = f"{_PATH}.GameModel"


class TestsGameStorage:
    @pytest.mark.parametrize("model_return", [None, MagicMock()])
    @patch(_ModulePatch.GAME_MODEL, new_callable=MagicMock)
    def test__get(self, model, model_return):
        username = "test_username"
        model.get_or_none.return_value = model_return

        actual = GameStorage.get(username)

        model.get_or_none.assert_called_once_with(model.username == username)
        if model_return is None:
            assert actual is None
        else:
            assert actual == model_return.backup

    @patch(_ModulePatch.GAME_MODEL, new_callable=MagicMock)
    def test__put(self, model):
        username = MagicMock()
        backup = MagicMock()
        game = MagicMock()
        model.get_or_create.return_value = game, None

        GameStorage.put(username, backup)

        model.get_or_create.assert_called_once_with(username=username)
        game.save.assert_called_once_with()
        assert game.backup == backup

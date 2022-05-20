from unittest.mock import MagicMock

import pytest

from app.domain.interfaces import Observable


class TestsObservable:
    def test__add_observer(self):
        observer = MagicMock()
        observable_obj = Observable()

        observable_obj.add_observer(observer)

        assert len(observable_obj._observers) == 1
        assert observer in observable_obj._observers

    def test__remove_observer(self):
        observer = MagicMock()
        observable_obj = Observable()
        observable_obj._observers = {observer}

        observable_obj.remove_observer(observer)

        assert len(observable_obj._observers) == 0

    def test__remove_observer_with_exception(self):
        observable_obj = Observable()

        with pytest.raises(ValueError):
            observable_obj.remove_observer(observer=MagicMock())

    def test__notify(self):
        observers = [MagicMock(), MagicMock()]
        observable_obj = Observable()
        observable_obj._observers = set(observers)

        observable_obj.notify()

        for observer in observers:
            observer.handle_event.assert_called_once_with()

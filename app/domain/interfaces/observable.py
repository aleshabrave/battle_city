from functools import wraps
from typing import Any, Callable

from .observer import Observer


class Observable:
    """Абстрактный класс наблюдаемых объектов."""

    _observers: set[Observer] = set()

    def add_observer(self, observer: Observer) -> None:
        """Добавить наблюдателя."""
        self._observers.add(observer)

    def remove_observer(self, observer: Observer) -> None:
        """Удалить наблюдателя."""
        self._observers.remove(observer)

    def notify(self) -> None:
        """Оповестить наблюдателей."""
        for observer in self._observers:
            observer.handle_event()

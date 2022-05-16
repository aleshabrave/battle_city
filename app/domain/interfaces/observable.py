from functools import wraps
from typing import Any, Callable, List

from .observer import Observer


class Observable:
    """Абстрактный класс наблюдаемых объектов."""

    observers: List[Observer] = []

    def add_observer(self, observer: Observer) -> None:
        """Добавить наблюдателя."""

        self.observers.append(observer)

    def remove_observer(self, observer: Observer) -> None:
        """Удалить наблюдателя."""

        self.observers.remove(observer)

    @staticmethod
    def notify(method: Callable) -> Callable:
        """Оповестить наблюдателей."""

        @wraps(method)
        def wrapper(*args, **kwargs) -> Any:
            result = method(*args, **kwargs)
            if isinstance(args[0], Observable):
                for observer in args[0].observers:
                    observer.handle_event()
            return result

        return wrapper

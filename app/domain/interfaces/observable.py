from typing import Any, Callable, Dict, List, Tuple

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

        def wrapper(*args: Tuple, **kwargs: Dict) -> Any:
            result = method(*args, **kwargs)

            for observer in args[0].observers:
                observer.handle_event(method.__name__)
            return result

        return wrapper

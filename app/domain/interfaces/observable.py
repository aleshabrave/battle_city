from .observer import Observer


class Observable:
    """Абстрактный класс наблюдаемых объектов."""

    _observers: list[Observer] = list()

    def add_observer(self, observer: Observer) -> None:
        """Добавить наблюдателя."""
        self._observers.append(observer)

    def remove_observer(self, observer: Observer) -> None:
        """Удалить наблюдателя."""
        self._observers.remove(observer)

    def notify(self) -> None:
        """Оповестить наблюдателей."""
        for observer in self._observers:
            observer.handle_event()

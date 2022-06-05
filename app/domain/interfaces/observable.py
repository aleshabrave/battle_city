from .observer import Observer


class Observable:
    """Interface for observale entities."""

    _observers: list[Observer] = list()

    def add_observer(self, observer: Observer) -> None:
        """Add observer."""
        self._observers.append(observer)

    def remove_observer(self, observer: Observer) -> None:
        """Remove observer."""
        self._observers.remove(observer)

    def notify(self) -> None:
        """Notify all observers"""
        for observer in self._observers:
            observer.handle_event()

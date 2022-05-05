from abc import ABC, abstractmethod


class Observer(metaclass=ABC):
    """Интерфейс наблюдателя."""

    @abstractmethod
    def handle_event(self, name: str) -> None:
        """Обработать событие."""

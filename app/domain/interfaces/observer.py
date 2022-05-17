from abc import abstractmethod


class Observer:
    """Интерфейс наблюдателя."""

    @abstractmethod
    def handle_event(self) -> None:
        """Обработать событие."""

from abc import abstractmethod


class Observer:
    """Interface for observer."""

    @abstractmethod
    def handle_event(self) -> None:
        """Handle event."""

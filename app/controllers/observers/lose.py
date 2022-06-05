from dataclasses import dataclass

from app.domain import Game, Level
from app.domain.enums import GameState, LevelState
from app.domain.interfaces import Living, Observer


@dataclass
class LoseObserver(Observer):
    """Observer, which checks castle and player."""

    _entities: list[Living]
    _level: Level
    _game: Game

    def handle_event(self) -> None:
        """Handle event - check on lose state."""

        for entity in self._entities:
            if not entity.is_available():
                self._clear()
                self._game.state = GameState.FINISHED
                self._level.state = LevelState.LOSE
                return

    def _clear(self) -> None:
        """Unsubscribe enemies."""
        for entity in self._entities:
            entity.remove_observer(self)

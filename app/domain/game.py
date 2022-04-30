from dataclasses import dataclass

from app.domain.data.enums import GameResult, GameState
from app.domain.map import Map


@dataclass
class Game:
    """Класс игры."""

    game_map: Map
    state: GameState = GameState.PAUSE
    game_result: GameResult = GameResult.UNDEFINED

from dataclasses import dataclass

from app.domain.data.enums import GameState, GameResult
from app.domain.map import Map


@dataclass
class Game:
    """Класс игры."""

    castle_name: str
    game_map: Map
    state: GameState = GameState.PAUSE
    game_result: GameResult = GameResult.UNDEFINED

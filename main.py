from app.domain import Game
from app.domain.data import GameResult
from app.domain.data.enums import GameState
from app.levels import parser
from app.main_loop import MainLoop

if __name__ == "__main__":
    # TODO переход на след уровни
    game = Game(
        parser.parse_map("./levels/wall_level.txt"),
        state=GameState.PLAY,
        game_result=GameResult.UNDEFINED,
    )
    MainLoop(tick_duration_secs=0.5, game=game)

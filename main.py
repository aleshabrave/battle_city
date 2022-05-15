from PyQt5.QtCore import QPoint, QRect

from app.controllers.game_controller import GameController
from app.controllers.map_controller import MapController
from app.domain import Game
from app.domain.data import GameResult
from app.domain.data.enums import GameState
from app.levels import parser
from app.main_loop import MainLoop


def main():
    _map = parser.parse_map("./levels/wall_level.txt")
    game = Game(
        _map,
        state=GameState.PLAY,
        game_result=GameResult.UNDEFINED,
    )
    MainLoop(
        game_controller=GameController(game, MapController(_map)),
        tick_duration_secs=0.3,
        window_size=QRect(QPoint(0, 0), QPoint(1000, 1000)),
    ).start()


if __name__ == "__main__":
    main()

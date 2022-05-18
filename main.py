from PyQt5.QtCore import QPoint, QRect

from app.controllers.game_controller import GameController
from app.domain.game import Game
from app.levels.generator import LevelGenerator
from app.main_loop import MainLoop


def main():
    level_generator = LevelGenerator()
    game = Game(level_generator.generate())
    game_controller = GameController(game)
    MainLoop(game_controller, 0.1, QRect(QPoint(0, 0), QPoint(1000, 1000))).start()


"""
def main():
    _map = parser.parse_map("./levels/empty_level.txt")
    game = Game(
        _map,
        state=GameState.PLAY,
        game_result=GameResult.UNDEFINED,
    )
    MainLoop(
        game_controller=GameController(game, MapController(_map)),
        tick_duration_secs=0.1,
        window_size=QRect(QPoint(0, 0), QPoint(1000, 1000)),
    ).start()
"""

if __name__ == "__main__":
    main()

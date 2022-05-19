from PyQt5.QtCore import QPoint, QRect

from app.controllers.game_controller import GameController
from app.domain.game import Game
from app.levels.generator import LevelGenerator
from app.main_loop import MainLoop


def main():
    level_generator = LevelGenerator()
    game = Game(level_generator.generate())
    game_controller = GameController(game)

    MainLoop(game_controller, 0.1, QRect(QPoint(0, 0), QPoint(256, 256))).start()


if __name__ == "__main__":
    main()

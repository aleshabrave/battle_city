from app.db.storage import GameStorage
from app.domain.enums import GameState
from app.domain.game import Game


def main():
    from app.db import migration

    migration.on_app_start()
    print(GameStorage.get("aboba"))
    # GameStorage.put("aboba", Game([], 0, GameState.FINISHED))
    # level_generator = GameGenerator()
    # game = Game(level_generator.generate())
    # game_controller = GameController(game)

    # MainLoop(game_controller, 0.1, QRect(QPoint(0, 0), QPoint(512, 512))).start()


if __name__ == "__main__":
    main()

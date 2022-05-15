from PyQt5.QtGui import QImage


class Images:
    _paths_to_images: dict[str, list[str]] = None

    @staticmethod
    def _add_paths_to_images() -> None:
        Images._paths_to_images = dict()
        Images._add_paths_to_images_for_wall()
        Images._add_paths_to_images_for_enemy()
        Images._add_paths_to_images_for_player()
        Images._add_paths_to_images_for_bullets()

    @staticmethod
    def _add_paths_to_images_for_player() -> None:
        Images._paths_to_images["player_tank"] = [
            r".\app\ui\spites\player\player1",
            r".\app\ui\spites\player\player2",
        ]

    @staticmethod
    def _add_paths_to_images_for_enemy() -> None:
        Images._paths_to_images["enemy_tank"] = [
            r".\app\ui\spites\enemy\enemy1",
            r".\app\ui\spites\enemy\enemy2",
        ]

    @staticmethod
    def _add_paths_to_images_for_wall() -> None:
        Images._paths_to_images["default_wall"] = [r".\app\ui\spites\wall\wall.png"]

    @staticmethod
    def _add_paths_to_images_for_bullets() -> None:
        Images._paths_to_images["enemy_bullet"] = [r".\app\ui\spites\bullet\bullet.png"]
        Images._paths_to_images["player_bullet"] = [
            r".\app\ui\spites\bullet\bullet.png"
        ]

    @staticmethod
    def get_images(entity_name: str) -> list[QImage]:
        if Images._paths_to_images is None:
            Images._add_paths_to_images()
        return list(map(QImage, Images._paths_to_images[entity_name]))

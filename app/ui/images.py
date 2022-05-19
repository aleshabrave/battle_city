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
        Images._add_paths_to_images_for_castle()

    @staticmethod
    def _add_paths_to_images_for_player() -> None:
        Images._paths_to_images["player"] = [
            r".\app\ui\spites\player\player1_32x32",
            r".\app\ui\spites\player\player2_32x32",
        ]

    @staticmethod
    def _add_paths_to_images_for_enemy() -> None:
        Images._paths_to_images["enemy_tank"] = [
            r".\app\ui\spites\enemy\enemy1_32x32",
            r".\app\ui\spites\enemy\enemy2_32x32",
        ]

    @staticmethod
    def _add_paths_to_images_for_wall() -> None:
        Images._paths_to_images["default_wall"] = [
            r".\app\ui\spites\wall\wall_32x32.png"
        ]

    @staticmethod
    def _add_paths_to_images_for_castle() -> None:
        Images._paths_to_images["castle"] = [r".\app\ui\spites\castle\castle_32x32.png"]

    @staticmethod
    def _add_paths_to_images_for_bullets() -> None:
        Images._paths_to_images["enemy_bullet"] = [
            r".\app\ui\spites\bullet\enemy_bullet_8x8.png"
        ]
        Images._paths_to_images["player_bullet"] = [
            r".\app\ui\spites\bullet\player_bullet_8x8.png"
        ]

    @staticmethod
    def get_images(entity_name: str) -> list[QImage]:
        if Images._paths_to_images is None:
            Images._add_paths_to_images()
        return list(map(QImage, Images._paths_to_images[entity_name]))

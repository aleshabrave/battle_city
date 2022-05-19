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
            r".\app\ui\spites\player\player1_16x16",
            r".\app\ui\spites\player\player2_16x16",
        ]

    @staticmethod
    def _add_paths_to_images_for_enemy() -> None:
        Images._paths_to_images["enemy_tank"] = [
            r".\app\ui\spites\enemy\enemy1_16x16",
            r".\app\ui\spites\enemy\enemy2_16x16",
        ]

    @staticmethod
    def _add_paths_to_images_for_wall() -> None:
        Images._paths_to_images["default_wall"] = [
            r".\app\ui\spites\wall\wall_16x16.png"
        ]

    @staticmethod
    def _add_paths_to_images_for_castle() -> None:
        Images._paths_to_images["castle"] = [r".\app\ui\spites\castle\castle16x16.png"]

    @staticmethod
    def _add_paths_to_images_for_bullets() -> None:
        Images._paths_to_images["enemy_bullet"] = [
            r".\app\ui\spites\bullet\enemy_bullet_4x4.png"
        ]
        Images._paths_to_images["player_bullet"] = [
            r".\app\ui\spites\bullet\player_bullet_4x4.png"
        ]

    @staticmethod
    def get_images(entity_name: str) -> list[QImage]:
        if Images._paths_to_images is None:
            Images._add_paths_to_images()
        return list(map(QImage, Images._paths_to_images[entity_name]))

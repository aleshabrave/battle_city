from PyQt5.QtGui import QImage


class Images:
    """Constant images."""

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
        Images._paths_to_images["player_default_tank"] = [
            r"./app/ui/sprites/player/player_default_tank2_32x32.png",
            r"./app/ui/sprites/player/player_default_tank1_32x32.png",
        ]
        Images._paths_to_images["player_big_bullet_tank"] = [
            r"./app/ui/sprites/player/player_big_bullet_tank2_32x32.png",
            r"./app/ui/sprites/player/player_big_bullet_tank1_32x32.png",
        ]
        Images._paths_to_images["player_fast_bullet_tank"] = [
            r"./app/ui/sprites/player/player_fast_bullet_tank2_32x32.png",
            r"./app/ui/sprites/player/player_fast_bullet_tank1_32x32.png",
        ]
        Images._paths_to_images["player_healthy_tank"] = [
            r"./app/ui/sprites/player/player_healthy_tank2_32x32.png",
            r"./app/ui/sprites/player/player_healthy_tank1_32x32.png",
        ]

    @staticmethod
    def _add_paths_to_images_for_enemy() -> None:
        Images._paths_to_images["enemy_default_tank"] = [
            r"./app/ui/sprites/enemy/enemy_default_tank2_32x32.png",
            r"./app/ui/sprites/enemy/enemy_default_tank1_32x32.png",
        ]
        Images._paths_to_images["enemy_big_bullet_tank"] = [
            r"./app/ui/sprites/enemy/enemy_big_bullet_tank2_32x32.png",
            r"./app/ui/sprites/enemy/enemy_big_bullet_tank1_32x32.png",
        ]
        Images._paths_to_images["enemy_fast_bullet_tank"] = [
            r"./app/ui/sprites/enemy/enemy_fast_bullet_tank2_32x32.png",
            r"./app/ui/sprites/enemy/enemy_fast_bullet_tank1_32x32.png",
        ]
        Images._paths_to_images["enemy_healthy_tank"] = [
            r"./app/ui/sprites/enemy/enemy_healthy_tank2_32x32.png",
            r"./app/ui/sprites/enemy/enemy_healthy_tank1_32x32.png",
        ]

    @staticmethod
    def _add_paths_to_images_for_wall() -> None:
        Images._paths_to_images["default_wall"] = [
            r"./app/ui/sprites/wall/wall_32x32.png"
        ]

    @staticmethod
    def _add_paths_to_images_for_castle() -> None:
        Images._paths_to_images["castle"] = [
            r"./app/ui/sprites/castle/castle_32x32.png"
        ]

    @staticmethod
    def _add_paths_to_images_for_bullets() -> None:
        Images._paths_to_images["enemy_bullet"] = [
            r"./app/ui/sprites/bullet/enemy_bullet_8x8.png"
        ]
        Images._paths_to_images["player_bullet"] = [
            r"./app/ui/sprites/bullet/player_bullet_8x8.png"
        ]

    @staticmethod
    def get_images(name: str) -> list[QImage]:
        """Get images by name."""
        if Images._paths_to_images is None:
            Images._add_paths_to_images()
        return list(map(QImage, Images._paths_to_images[name]))

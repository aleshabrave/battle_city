from PyQt5.QtGui import QImage


class Images:
    _paths_to_images: dict[str, list[QImage]] = None

    @staticmethod
    def _add_paths_to_images() -> None:
        Images._paths_to_images = dict()
        Images._add_paths_to_images_for_wall()
        Images._add_paths_to_images_for_tank()

    @staticmethod
    def _add_paths_to_images_for_tank() -> None:
        Images._paths_to_images["default_tank"] = [
            QImage(r".\app\ui\spites\tank\tank1"),
            QImage(r".\app\ui\spites\tank\tank2"),
        ]

    @staticmethod
    def _add_paths_to_images_for_wall() -> None:
        Images._paths_to_images["default_wall"] = [
            QImage(r".\app\ui\spites\wall\wall.png")
        ]

    @staticmethod
    def get_images(entity_name: str) -> list[QImage]:
        if Images._paths_to_images is None:
            Images._add_paths_to_images()
        return Images._paths_to_images[entity_name]

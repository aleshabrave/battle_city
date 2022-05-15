from PyQt5.QtGui import QKeyEvent

from app.controllers.map_controller import MapController


class UserController:
    def __init__(self, map_controller: MapController):
        self._map_controller = map_controller

    def handle_event(self, event: QKeyEvent) -> None:
        print(f'FROM UserController: {chr(event.key())}')

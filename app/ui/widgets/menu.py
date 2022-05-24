from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QBoxLayout

from app.constants import Default


class MenuWidget:
    def __init__(self, window: QMainWindow, widget: QWidget):
        self.window = window
        self.widget = widget
        self.widget.setStyleSheet(
            f"background-image: url({Default.PATH_TO_MM_BACKGROUND});"
        )
        self.initButtons()

    def initButtons(self):
        new_game_button = QPushButton(Default.NEW_GAME_BUTTON_NAME, self.widget)
        continue_game_button = QPushButton(
            Default.CONTINUE_GAME_BUTTON_NAME, self.widget
        )

        button_layout = QBoxLayout(QBoxLayout.Direction.TopToBottom)
        button_layout.addWidget(new_game_button)
        button_layout.addWidget(continue_game_button)

        button_layout.setGeometry(QRect(206, 300, 100, 100))

        new_game_button.clicked.connect(self.newGameButtonClicked)
        continue_game_button.clicked.connect(self.continueGameButtonClicked)

    def newGameButtonClicked(self):
        pass

    def continueGameButtonClicked(self):
        pass

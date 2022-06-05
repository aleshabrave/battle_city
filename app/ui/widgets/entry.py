from typing import TYPE_CHECKING

from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QFont, QKeyEvent
from PyQt5.QtWidgets import QBoxLayout, QLabel, QLineEdit, QPushButton, QWidget

from app.constants import Default
from app.controllers.game_controller import GameController

if TYPE_CHECKING:
    from app.ui.main_window import MainWindow


class EntryWidget(QWidget):
    text: str = None

    def __init__(self, parent: "MainWindow"):
        super(EntryWidget, self).__init__(parent)
        self.main_window = parent

        self.bg_label = QLabel(self)
        self.entry_label = QLabel(self)
        self.qle = QLineEdit(self)
        self.go_button = QPushButton(Default.GO_BUTTON, self)
        self.layout = QBoxLayout(QBoxLayout.Direction.TopToBottom)

    def init(self):
        self.bg_label.resize(612, 512)
        self.bg_label.setStyleSheet(
            f"background-image: url({Default.PATH_TO_ENTRY_BACKGROUND});"
        )

        self.entry_label.setFont(QFont("Verdana", 24, QFont.Bold))
        self.entry_label.setText("USERNAME")
        self.entry_label.setMargin(8)

        self.qle.resize(100, 50)
        self.qle.setMaxLength(12)
        self.qle.textChanged[str].connect(self.onChanged)

        self.go_button.clicked.connect(self.goButtonClicked)

        self.layout.addWidget(self.entry_label)
        self.layout.addWidget(self.qle)
        self.layout.addWidget(self.go_button)
        self.layout.setGeometry(QRect(196, 100, 220, 100))

    def onChanged(self, text):
        self.text = text

    def goButtonClicked(self):
        if self.text is None or len(self.text) == 0:
            return
        self.main_window.username = self.text
        self.main_window.game_controller = GameController(0.1, self.text)
        self.main_window.display(1)

    def keyPressEvent(self, event: QKeyEvent) -> None:
        key = event.key()
        if key == Qt.Key_Enter or key == Qt.Key_Return:
            self.go_button.click()

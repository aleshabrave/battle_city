import sys
import traceback

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QMessageBox

from app.ui.main_window import MainWindow
from app.db import migration


def log_uncaught_exceptions(ex_cls, ex, tb):
    text = "{}: {}:\n".format(ex_cls.__name__, ex)

    text += "".join(traceback.format_tb(tb))

    print(text)
    QMessageBox.critical(None, "Error", text)

    sys.exit()


def main():
    with migration.on_app_start():
        sys.excepthook = log_uncaught_exceptions
        app = QApplication(sys.argv)
        win = MainWindow(QSize(512, 512))
        win.show()
        sys.exit(app.exec_())


if __name__ == "__main__":
    main()

import sys
import traceback

from PyQt5.QtWidgets import QApplication, QMessageBox

from app.db.models import try_create_tables
from app.ui.main_window import MainWindow


def log_uncaught_exceptions(ex_cls, ex, tb):
    text = "{}: {}:\n".format(ex_cls.__name__, ex)

    text += "".join(traceback.format_tb(tb))

    print(text)
    QMessageBox.critical(None, "Error", text)

    sys.exit()


def main():
    sys.excepthook = log_uncaught_exceptions
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()

    try:
        try_create_tables()
        sys.exit(app.exec_())
    except ConnectionError:
        QMessageBox.critical(
            None, "Internal error", f"Refused connection with database."
        )
        app.exit()


if __name__ == "__main__":
    main()

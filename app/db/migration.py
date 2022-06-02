from contextlib import contextmanager

from app.db.models import GameModel, postgr_db


@contextmanager
def on_app_start():
    try:
        with postgr_db.atomic():
            postgr_db.create_tables([GameModel])
    finally:
        yield
        postgr_db.close()

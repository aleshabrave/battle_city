from app.db.models import postgr_db, GameModel


def on_app_start():
    if not postgr_db.connect():
        raise ValueError("Bad connection with db, check your env.json.")

    with postgr_db.connection_context():
        postgr_db.create_tables([GameModel])

    postgr_db.close()

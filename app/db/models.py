from peewee import CharField, Model, Proxy, OperationalError
from playhouse.fields import PickleField

from app.db import dependencies

db_proxy = Proxy()


class BaseModel(Model):
    """Base model."""

    class Meta:
        database = db_proxy


class GameModel(BaseModel):
    """Game model."""

    username = CharField(primary_key=True)
    backup = PickleField(default=None)


def init_db():
    """Initialize db."""
    db = dependencies.get_db()
    db_proxy.initialize(db)
    try:
        with db.atomic():
            db.create_tables([GameModel])
    except OperationalError:
        raise ConnectionError("Can not connect to database.")
    finally:
        db.close()

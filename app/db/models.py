import json

import peewee
from peewee import CharField, Model, PostgresqlDatabase
from playhouse.fields import PickleField

with open("env.json", "r") as f:
    settings = json.load(f)

postgr_db = PostgresqlDatabase(**settings)


class BaseModel(Model):
    """Базовая моделька."""

    class Meta:
        database = postgr_db


class GameModel(BaseModel):
    """Моделька игры."""

    username = CharField(primary_key=True)
    backup = PickleField()


def try_create_tables():
    try:
        with postgr_db.atomic():
            postgr_db.create_tables([GameModel])
    except peewee.OperationalError:
        raise ConnectionError("Can not connect to database.")
    finally:
        postgr_db.close()

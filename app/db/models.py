import json

from peewee import Model, PostgresqlDatabase, CharField
from playhouse.fields import PickleField

with open("env.json", "r") as f:
    settings = json.load(f)

postgr_db = PostgresqlDatabase(**settings)


class BaseModel(Model):
    class Meta:
        database = postgr_db


class GameModel(BaseModel):
    username = CharField(primary_key=True, unique=True)
    backup = PickleField()

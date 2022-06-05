import json

from peewee import PostgresqlDatabase


def _get_db_connector():
    """Get db connector."""

    with open("env.json", "r") as f:
        settings = json.load(f)
    db = PostgresqlDatabase(**settings)

    while True:
        yield db


def get_db(connector=_get_db_connector()):
    """Get db."""
    return next(connector)

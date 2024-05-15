from peewee import CharField, UUIDField

from src.database.models import BaseDbModel


class MaleLastNames(BaseDbModel):
    id = UUIDField(primary_key=True)
    name = CharField()

from peewee import UUIDField, CharField

from src.database.models import BaseDbModel


class FemaleNames(BaseDbModel):
    id = UUIDField(primary_key=True)
    name = CharField()

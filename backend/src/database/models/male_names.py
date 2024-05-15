from peewee import UUIDField, CharField

from src.database.models import BaseDbModel


class MaleNames(BaseDbModel):
    id = UUIDField(primary_key=True)
    name = CharField()

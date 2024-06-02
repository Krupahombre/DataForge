from peewee import DateTimeField, UUIDField

from src.database.models import BaseDbModel


class AddressMigrations(BaseDbModel):
    id = UUIDField(primary_key=True)
    date = DateTimeField()

from peewee import UUIDField, CharField

from src.database.models import BaseDbModel


class BankProviders(BaseDbModel):
    id = UUIDField(primary_key=True)
    name = CharField()
    number = CharField()
    address = CharField()

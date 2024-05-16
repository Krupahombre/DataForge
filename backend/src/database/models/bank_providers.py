from peewee import UUIDField, CharField, IntegerField

from src.database.models import BaseDbModel


class BankProviders(BaseDbModel):
    id = UUIDField(primary_key=True)
    internal_id = IntegerField()
    name = CharField()
    number = CharField()
    address = CharField()

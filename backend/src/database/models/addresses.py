from peewee import UUIDField, CharField

from src.database.models import BaseDbModel


class Addresses(BaseDbModel):
    id = UUIDField(primary_key=True)
    street = CharField()
    number = CharField()
    postal_code = CharField()
    gus_terc = CharField()
    settlement = CharField()

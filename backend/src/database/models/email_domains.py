from peewee import CharField, UUIDField
from src.database.models import BaseDbModel


class EmailDomains(BaseDbModel):
    id = UUIDField(primary_key=True)
    domain = CharField()

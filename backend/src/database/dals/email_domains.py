from peewee import CharField, UUIDField
from src.database.models import BaseModel


class EmailDomains(BaseModel):
    Id = UUIDField(primary_key=True)
    Domain = CharField()

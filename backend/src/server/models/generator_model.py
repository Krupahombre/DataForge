from typing import List

from fastapi import Query
from pydantic import BaseModel


class Field(BaseModel):
    name: str
    type: str


class Table(BaseModel):
    name: str
    fields: List[Field]


class GeneratorModel(BaseModel):
    tables: List[Table]
    records: int = Query(None)

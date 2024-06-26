from typing import List

from fastapi import Query
from pydantic import BaseModel

from src.utils.enums.response_format import ResponseFormat


class Field(BaseModel):
    name: str
    type: str


class Table(BaseModel):
    name: str
    fields: List[Field]


class GeneratorModel(BaseModel):
    tables: List[Table]
    records: int = Query(None)
    format: ResponseFormat = Query(None)

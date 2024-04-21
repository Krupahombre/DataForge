from typing import List

from fastapi import Query
from pydantic import BaseModel


class GeneratorModel(BaseModel):
    generators_list: List[str] = Query(None)
    records: int = Query(None)

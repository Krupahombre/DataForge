import random

from src.database.models import BaseDbModel


def get_batch(model: BaseDbModel, size: int = 1000, offset: int = 0) -> list[BaseDbModel]:
    out_list = [model.select(model).limit(size).offset(offset)]
    random.shuffle(out_list)
    return out_list


def get_count(model: BaseDbModel) -> int:
    return model.select().count()


def get_all(model: BaseDbModel) -> list[BaseDbModel]:
    return model.select(model)

import random
from datetime import datetime

from peewee import DoesNotExist, PeeweeException

from src.database.models import BaseDbModel
from src.database.models.address_migrations import AddressMigrations


def get_batch(model: BaseDbModel, size: int = 1000, offset: int = 0) -> list[BaseDbModel]:
    out_list = [model.select(model).limit(size).offset(offset)]
    random.shuffle(out_list)
    return out_list


def get_count(model: BaseDbModel) -> int:
    return model.select().count()


def get_all(model: BaseDbModel) -> list[BaseDbModel]:
    return model.select(model)


def delete_all(model: BaseDbModel):
    model.delete().execute()


def get_last_migration() -> AddressMigrations | None:
    try:
        return (
            AddressMigrations.select()
            .order_by(AddressMigrations.date.desc())
            .get()
        )
    except DoesNotExist:
        return None


def add_migration() -> AddressMigrations | None:
    return AddressMigrations.create(
        date=datetime.now()
    )


def insert_bulk(model: BaseDbModel, data: list[dict]) -> int | None:
    return model.insert_many(data).execute()

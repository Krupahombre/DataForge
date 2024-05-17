import logging
import random

from fastapi import HTTPException
from starlette import status

from src.generator import GENERATOR_FIELDS, GENERATORS

from src.server.models.generator_model import GeneratorModel, Table, Field

from src.generator.bank.bank_data_generator import bank_data_generator

logger = logging.getLogger("DataGeneratorService")
request_metadate = {}


def get_available_generators_list() -> dict[str, [list[str]]]:
    print(bank_data_generator.generate_name([1, 12, 3]))
    return GENERATOR_FIELDS


def generate_data(request: GeneratorModel):
    output = {}
    records_num = request.records
    tables = request.tables
    for table in tables:
        output.update(handle_table(table, records_num))
    return output


def handle_table(table: Table, records_num: int):
    columns = {}
    person_fields = [field for field in table.fields if field.type.startswith("person")]
    if person_fields:
        columns.update(handle_person_fields(person_fields, records_num))
    bank_fields = [field for field in table.fields if field.type.startswith("bank")]
    if bank_fields:
        columns.update(handle_bank_fields(bank_fields, records_num))
    other_fields = [field for field in table.fields if
                    not field.type.startswith("person") and not field.type.startswith("bank")]
    for field in other_fields:
        columns.update({(field.name, field.type), GENERATOR_FIELDS[field.type].generate(field.name, records_num)})
    return {table.name: columns}


def generate_seed_values_list(records_num: int, max_records: int) -> list:
    seed_list = random.sample(range(1, max_records + 1), records_num)
    random.shuffle(seed_list)
    return seed_list


def handle_bank_fields(fields: list[Field], records_num: int):
    if not fields:
        return
    generator = "bank"
    ibans = {}
    numbers = {}
    names = {}
    addresses = {}
    seed_list = generate_seed_values_list(records_num, bank_data_generator.get_num_of_data_records())
    field_types = [field.type.split(":")[1] for field in fields]
    if "name" in field_types:
        names = handle_field(generator, "bank:name", fields, records_num, seed_list, None)
    if "address" in field_types:
        addresses = handle_field(generator, "bank:address", fields, records_num, seed_list, None)
    if "number" in field_types:
        numbers = handle_field(generator, "bank:number", fields, records_num, seed_list, None)
    if "iban" in field_types:
        if not numbers:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid bank data field config for iban (number)"
            )
        ibans = handle_field(generator, "bank:iban", fields, records_num, seed_list, [numbers])
    return {**names, **addresses, **numbers, **ibans}


def handle_person_fields(fields: list[Field], records_num: int):
    if not fields:
        return
    generator = "person"
    sexes = {}
    birth_dates = {}
    first_names = {}
    last_names = {}
    pesels = {}
    emails = {}
    field_types = [field.type.split(":")[1] for field in fields]
    if "sex" in field_types:
        sexes = handle_field(generator, "person:sex", fields, records_num, None, None)

    if "birth_date" in field_types:
        birth_dates = handle_field(generator, "person:birth_date", fields, records_num, None, None)

    if "name" in field_types:
        if not sexes:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid person data field config for name (sex required)"
            )
        first_names = handle_field(generator, "person:name", fields, records_num, None, [sexes])

    if "last_name" in field_types:
        if not sexes:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid person data field config for last_name (sex required)"
            )
        last_names = handle_field(generator, "person:last_name", fields, records_num, None, [sexes])

    if "pesel" in field_types:
        if not sexes or not birth_dates:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid person data field config for pesel (birthdate and sex required)"
            )
        pesels = handle_field(generator, "person:pesel", fields, records_num, None, [birth_dates, sexes])

    if "email" in field_types:
        if not first_names or not last_names:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid person data field config for email (name and last_name required)"
            )
        emails = handle_field(generator, "person:email", fields, records_num, None, [first_names, last_names])

    return {**sexes, **birth_dates, **first_names, **last_names, **pesels, **emails}


def handle_field(generator: str, field_type: str, fields, records_num: int, seed_list: list = None, deps=None):
    if deps is None:
        deps = []
    field_name = next(field.name for field in fields if field.type == field_type)
    deps = [list(dep.values())[0] for dep in deps]
    return {(field_name, field_type): GENERATORS[generator].generate(field_type.split(":")[1], records_num, seed_list, deps)}

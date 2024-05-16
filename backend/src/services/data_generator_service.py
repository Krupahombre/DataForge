import logging

from fastapi import HTTPException
from starlette import status

from src.generator import GENERATOR_FIELDS, GENERATORS

from src.server.models.generator_model import GeneratorModel, Table, Field

logger = logging.getLogger("DataGeneratorService")
request_metadate = {}


def get_available_generators_list() -> dict[str, [list[str]]]:
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
    columns.update(handle_person_fields(person_fields, records_num))
    bank_fields = [field for field in table.fields if field.type == "bank"]
    columns.update(handle_bank_fields(bank_fields, records_num))
    other_fields = [field for field in table.fields if
                    not field.type.startswith("person") and not field.type.startswith("bank")]
    for field in other_fields:
        columns.update({(field.name, field.type), GENERATOR_FIELDS[field.type].generate(field.name, records_num)})
    return {table.name: columns}


def handle_bank_fields(fields: list[Field], records_num: int):
    # TODO Pętla -> powiąż dane bankowe csv -> patrz jakie kolumny
    return []


def handle_person_fields(fields: list[Field], records_num: int):
    if not fields:
        return
    sexes = {}
    birth_dates = {}
    first_names = {}
    last_names = {}
    pesels = {}
    emails = {}
    field_types = [field.type.split(":")[1] for field in fields]
    if "sex" in field_types:
        sexes = handle_person_field("person:sex", fields, records_num)

    if "birth_date" in field_types:
        birth_dates = handle_person_field("person:birth_date", fields, records_num)

    if "name" in field_types:
        if not sexes:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid person data field config for name (sex required)"
            )
        first_names = handle_person_field("person:name", fields, records_num, [sexes])

    if "last_name" in field_types:
        if not sexes:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid person data field config for last_name (sex required)"
            )
        last_names = handle_person_field("person:last_name", fields, records_num, [sexes])

    if "pesel" in field_types:
        if not sexes or not birth_dates:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid person data field config for pesel (birthdate and sex required)"
            )
        pesels = handle_person_field("person:pesel", fields, records_num, [birth_dates, sexes])

    if "email" in field_types:
        if not first_names or not last_names:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid person data field config for email (name and last_name required)"
            )
        emails = handle_person_field("person:email", fields, records_num, [first_names, last_names])

    return {**sexes, **birth_dates, **first_names, **last_names, **pesels, **emails}


def handle_person_field(field_type: str, fields, records_num: int, deps=None):
    if deps is None:
        deps = []
    field_name = next(field.name for field in fields if field.type == field_type)
    deps = [list(dep.values())[0] for dep in deps]
    return {(field_name, field_type): GENERATORS["person"].generate(field_type.split(":")[1], records_num, deps)}

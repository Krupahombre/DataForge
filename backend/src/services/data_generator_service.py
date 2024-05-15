from typing import List
import logging

from fastapi import HTTPException
from src.utils.enums.generators import Generators
from src.services.iban.iban_generator import iban_generator
from src.services.person.person_generator import person_generator
from starlette import status

from src.server.models.generator_model import GeneratorModel, Table, Field

logger = logging.getLogger("DataGeneratorService")
request_metadate = {}


def get_available_generators_list() -> dict[str, [list[str]]]:
    return GENERATOR_FIELDS


def generate_data(generator_data: GeneratorModel):
    request_types = generator_data.generators_list
    records_to_generate = generator_data.records

    if request_types is None:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Generators list cannot be empty!"
        )
    gen_types = []
    for generator in generators.keys():
        supported_datatypes = generator.get_supported_types()
        for sup_type in supported_datatypes:
            if sup_type in request_types:
                request_types.remove(sup_type)
                gen_types.append(sup_type)
        if gen_types:
            generators[generator] = gen_types
            gen_types = []

def handle_table(table: Table, records_num: int):
    columns = {}
    person_fields = [field for field in table.fields if field.type.startswith("person")]
    columns.update(handle_person_fields(person_fields, records_num))
    bank_fields = [field for field in table.fields if field.type == "bank"]
    columns.update(handle_bank_fields(bank_fields, records_num))
    other_fields = [field for field in table.fields if not field.type.startswith("person") and not field.type.startswith("bank")]
    for field in other_fields:
        columns.update((field.name, GENERATOR_FIELDS[field.type].generate(field.name, records_num)))
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
    generator = GENERATORS["person"]
    if "sex" in field_types:
        field_name = next(field.name for field in fields if field.type == "person:sex")
        sexes = {field_name: generator.generate("sex", records_num)}

    if "birth_date" in field_types:
        field_name = next(field.name for field in fields if field.type == "person:birth_date")
        birth_dates = {field_name: generator.generate("birth_date", records_num)}

    if "name" in field_types:
        if not sexes:
            raise Exception("Invalid person data field config")
        field_name = next(field.name for field in fields if field.type == "person:name")
        sexes_list = list(sexes.values())[0]
        first_names = {field_name: generator.generate("name", records_num, [sexes_list])}

    if "last_name" in field_types:
        if not sexes:
            raise Exception("Invalid person data field config")
        field_name = next(field.name for field in fields if field.type == "person:last_name")
        sexes_list = list(sexes.values())[0]
        last_names = {field_name: generator.generate("last_name", records_num, [sexes_list])}

    if "pesel" in field_types:
        if not sexes or not birth_dates:
            raise Exception("Invalid person data field config")
        field_name = next(field.name for field in fields if field.type == "person:pesel")
        sexes_list = list(sexes.values())[0]
        birth_dates_list = list(birth_dates.values())[0]
        pesels = {field_name: generator.generate("pesel", records_num, [birth_dates_list, sexes_list])}

    if "email" in field_types:
        if not first_names or not last_names:
            raise Exception("Invalid person data field config")
        field_name = next(field.name for field in fields if field.type == "person:email")
        first_names_list = list(first_names.values())[0]
        last_names_list = list(last_names.values())[0]
        emails = {field_name: generator.generate("email", records_num, [first_names_list, last_names_list])}

    output = {}
    output.update(sexes)
    output.update(birth_dates)
    output.update(first_names)
    output.update(last_names)
    output.update(pesels)
    output.update(emails)
    return output

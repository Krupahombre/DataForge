import logging
import random
from typing import Any

from fastapi import HTTPException
from starlette import status

from src.generator import GENERATOR_FIELDS, GENERATORS
from src.generator.bank.bank_data_generator import bank_data_generator
from src.server.models.generator_model import GeneratorModel, Table, Field

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

    address_fields = [field for field in table.fields if field.type.startswith("address")]
    if address_fields:
        columns.update(handle_address_fields(address_fields, records_num))

    vehicle_fields = [field for field in table.fields if field.type.startswith("vehicle")]
    if vehicle_fields:
        columns.update(handle_vehicle_fields(vehicle_fields, records_num))

    other_fields = [field for field in table.fields if is_other_field(field)]
    for field in other_fields:
        columns.update({(field.name, field.type), GENERATORS[field.type].generate(field.name, records_num)})
    return {table.name: columns}


def generate_seed_values_list(records_num: int, max_records: int) -> list:
    seed_list = random.sample(range(1, max_records + 1), records_num)
    random.shuffle(seed_list)
    return seed_list


def handle_address_fields(fields: list[Field], records_num: int):
    if not fields:
        return
    field_names = [field.type.split(":")[1] for field in fields]
    request_dicts = {(field.name, field.type): [] for field in fields}
    records = GENERATORS["address"].generate_subset(field_names, records_num)
    for record in records:
        for key, value in request_dicts.items():
            field_val = getattr(record, key[1].split(":")[1])
            value.append(field_val)

    return request_dicts


def handle_vehicle_fields(fields: list[Field], records_num: int):
    if not fields:
        return
    records = GENERATORS["vehicle"].generate_subset(None, records_num)
    request_dicts = {(field.name, field.type): [] for field in fields}
    for record in records:
        for key, value in request_dicts.items():
            field_val = record[key[1].split(":")[1]]
            value.append(field_val)

    return request_dicts


def handle_bank_fields(fields: list[Field], records_num: int):
    if not fields:
        return
    generator = "bank"
    ibans = {}
    numbers = {}
    names = {}
    addresses = {}
    card_providers = {}
    card_numbers = {}
    card_security_codes = {}
    card_expiry_dates = {}
    seed_list = generate_seed_values_list(records_num, bank_data_generator.get_num_of_data_records())
    field_types = [field.type.split(":")[1] for field in fields]
    if "name" in field_types:
        names = handle_field(generator, "bank:name", fields, records_num, seed_list, None)
    if "address" in field_types:
        addresses = handle_field(generator, "bank:address", fields, records_num, seed_list, None)
    if "number" in field_types:
        numbers = handle_field(generator, "bank:number", fields, records_num, seed_list, None)
    if "iban" in field_types:
        deps = [numbers] if numbers else None
        ibans = handle_field(generator, "bank:iban", fields, records_num, seed_list, deps)
    if "card_provider" in field_types:
        card_providers = handle_field(generator, "bank:card_provider", fields, records_num, None, None)
    if "card_number" in field_types:
        deps = [card_providers] if card_providers else None
        card_numbers = handle_field(generator, "bank:card_number", fields, records_num, None, deps)
    if "card_security_code" in field_types:
        card_security_codes = handle_field(generator, "bank:card_security_code", fields, records_num, None, None)
    if "card_expiry_date" in field_types:
        card_expiry_dates = handle_field(generator, "bank:card_expiry_date", fields, records_num, None, None)
    return {**names, **addresses, **numbers, **ibans, **card_numbers, **card_providers, **card_security_codes, **card_expiry_dates}


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
        deps = [sexes] if sexes else None
        first_names = handle_field(generator, "person:name", fields, records_num, None, deps)

    if "last_name" in field_types:
        deps = [sexes] if sexes else None
        last_names = handle_field(generator, "person:last_name", fields, records_num, None, deps)

    if "pesel" in field_types:
        deps = []
        if sexes:
            deps.append(sexes)
        if birth_dates:
            deps.append(birth_dates)
        pesels = handle_field(generator, "person:pesel", fields, records_num, None, deps)

    if "email" in field_types:
        deps = []
        if first_names:
            deps.append(first_names)
        if last_names:
            deps.append(last_names)
        emails = handle_field(generator, "person:email", fields, records_num, None, deps)

    return {**sexes, **birth_dates, **first_names, **last_names, **pesels, **emails}


def handle_field(generator: str, field_type: str, fields, records_num: int, seed_list: list = None, deps=None):
    if deps is None:
        deps = []
    field_name = next(field.name for field in fields if field.type == field_type)
    deps = [list(dep.values())[0] for dep in deps]
    return {
        (field_name, field_type): GENERATORS[generator].generate(field_type.split(":")[1], records_num, seed_list, deps)
    }


def is_other_field(field) -> bool:
    return (not field.type.startswith("person")
            and not field.type.startswith("bank")
            and not field.type.startswith("address")
            and not field.type.startswith("vehicle"))

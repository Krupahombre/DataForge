from src.generator.address.address_generator import AddressDataGenerator, address_data_generator
from src.generator.bank.bank_data_generator import BankDataGenerator, bank_data_generator
from src.generator.person.person_generator import PersonGenerator, person_generator

GENERATOR_FIELDS = {
    "bank": BankDataGenerator.get_fields(),
    "person": PersonGenerator.get_fields(),
    "address": AddressDataGenerator.get_fields(),
}


GENERATORS = {
    "bank": bank_data_generator,
    "person": person_generator,
    "address": address_data_generator
}

FIELD_TYPES = {
    "person": {
        "name": str,
        "last_name": str,
        "sex": str,
        "birth_date": str,
        "pesel": int,
        "email": str,
    },
    "bank": {
        "name": str,
        "address": str,
        "number": str,
        "iban": str,
        "card_number": str,
        "card_security_code": str,
        "card_expiry_date": str,
        "card_provider": str,
    },
    "address": {
        "street": str,
        "number": str,
        "postal_code": str,
        "gus_terc": str,
        "settlement": str,
    }
}

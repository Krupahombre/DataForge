from src.generator.bank.bank_data_generator import BankDataGenerator, bank_data_generator
from src.generator.person.person_generator import PersonGenerator, person_generator
from src.generator.person.email_generator import EmailGenerator
from src.generator.person.pesel_generator import PeselGenerator

GENERATOR_FIELDS = {
    "bank": BankDataGenerator.get_fields(),
    "person": PersonGenerator.get_fields(),
}


GENERATORS = {
    "bank": bank_data_generator,
    "person": person_generator,
}
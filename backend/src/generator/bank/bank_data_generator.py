import logging
import random

from pydantic import BaseModel

from src.database.generic_dal import get_all
from src.database.models.bank_providers import BankProviders
from src.generator.bank.iban_generator import iban_generator
from src.generator.base_generator import BaseGenerator

fields = ["name", "address", "number", "iban"]


class BankDataModel(BaseModel):
    iban: str = None


class BankDataGenerator(BaseGenerator):
    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger('BankDataGenerator')
        self.supported_types = ["bank"]
        self.bank_institutions = get_all(BankProviders)
        self.first_field_picked_idx = []
        self.max_data_records = 2808

    def get_supported_types(self) -> list[str]:
        return self.supported_types

    def get_num_of_data_records(self) -> int:
        return self.max_data_records

    @staticmethod
    def get_fields() -> list[str]:
        return fields

    def get_name(self) -> str:
        return "bank"

    def generate(self, field: str, records_to_generate: int, seed_list: list = None, metadata: list = None) -> list:
        if field not in fields:
            self.logger.exception(f"Unsupported type {type}")
            raise Exception(f"Unsupported type {type}")
        self.bank_institutions = list(self.bank_institutions)
        match field:
            case "iban":
                return self.generate_iban(metadata[0], records_to_generate)
            case "name":
                return self.generate_name(seed_list)
            case "address":
                return self.generate_address(seed_list)
            case "number":
                return self.generate_number(seed_list)

    def generate_iban(self, numbers: list, records_to_generate: int) -> list:
        if len(numbers) != records_to_generate:
            self.logger.exception("No provided metadata for iban")
            raise Exception("No provided metadata for iban")
        out = []
        for i in range(0, records_to_generate):
            out.append(iban_generator.generate_iban(numbers[i]))
        return out

    def generate_number(self, seed_list: list) -> list:
        out = []
        for i in seed_list:
            data = next((bank for bank in self.bank_institutions if bank.internal_id == i), None)
            out.append(data.number)
        return out

    def generate_name(self, seed_list: list) -> list:
        out = []
        for i in seed_list:
            data = next((bank for bank in self.bank_institutions if bank.internal_id == i), None)
            out.append(data.name)
        return out

    def generate_address(self, seed_list: list) -> list:
        out = []
        for i in seed_list:
            data = next((bank for bank in self.bank_institutions if bank.internal_id == i), None)
            out.append(data.address)
        return out


bank_data_generator = BankDataGenerator()

import logging
import random
import string
from typing import List

from pydantic import BaseModel

from src.database.generic_dal import get_all
from src.database.models.bank_providers import BankProviders
from src.generator.base_generator import BaseGenerator

fields = ["iban", "bank_name", "bank_address"]


class BankDataModel(BaseModel):
    iban: str = None


class BankDataGenerator(BaseGenerator):
    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger('BankDataGenerator')
        # self.iban_prefix = 'PL00'
        # self.bank_num_length = 16
        self.supported_types = ["bank"]
        self.bank_institutions = get_all(BankProviders)

    def get_supported_types(self) -> list[str]:
        return self.supported_types

    @staticmethod
    def get_fields() -> list[str]:
        return fields

    def get_name(self) -> str:
        return "BankData"

    def generate(self, field: str, records_to_generate: int, metadata: list = None) -> list:
        if field not in fields:
            self.logger.exception(f"Unsupported type {type}")
            raise Exception(f"Unsupported type {type}")
        match field:
            case "iban":
                pass
            case "bank_name":
                pass
            case "bank_address":
                pass


bank_data_generator = BankDataGenerator()

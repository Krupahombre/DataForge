import logging
import random

from pydantic import BaseModel

from src.database.generic_dal import get_all
from src.database.models.addresses import Addresses
from src.generator.base_generator import BaseGenerator

fields = ["street", "number", "postal_code", "gus_terc", "settlement"]


class AddressDataModel(BaseModel):
    street: str = None
    number: str = None
    postal_code: str = None
    gus_terc: str = None
    settlement: str = None


class AddressDataGenerator(BaseGenerator):
    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger('AddressDataGenerator')
        self.supported_types = ["address"]
        self.addresses = get_all(Addresses)

    def get_supported_types(self) -> list[str]:
        return self.supported_types

    @staticmethod
    def get_fields() -> list[str]:
        return fields

    @staticmethod
    def get_name() -> str:
        return "address"

    def generate_subset(self, subset: list[str], records_to_generate: int) -> list:
        out = []
        for i in range(0, records_to_generate):
            address = random.choice(self.addresses)
            curr_record = AddressDataModel()
            for field in subset:
                if field not in fields:
                    self.logger.exception(f"Unsupported field {field}")
                    raise Exception(f"Unsupported field {field}")
                value = getattr(address, field)
                setattr(curr_record, field, value)
            out.append(curr_record)
        return out


address_data_generator = AddressDataGenerator()

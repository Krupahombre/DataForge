import logging
import csv
import random
import string
from typing import List

from pydantic import BaseModel
from src.services.base_generator import BaseGenerator


class IBANModel(BaseModel):
    iban: str = None


class IBANGenerator(BaseGenerator):
    def __init__(self):
        # TODO change after db setup
        self.bank_institutions_file = './src/services/iban/data/bank_institutions.csv'
        self.bank_institutions = self.load_data_from_file(self.bank_institutions_file)
        self.logger = logging.getLogger('IBANGenerator')
        self.iban_prefix = 'PL00'
        self.bank_num_length = 16
        self.supported_types = ["iban"]

    def get_supported_types(self) -> list[str]:
        return self.supported_types

    def generate(self, types: list[str], records_to_generate: int) -> dict[str, any]:
        for type in types:
            if type not in self.supported_types:
                raise Exception(f"Unsupported type {type}")
        return dict([("iban", self.generate_iban(records_to_generate))])

    def generate_random_account_number(self):
        return ''.join(random.choices(string.digits, k=self.bank_num_length))

    @staticmethod
    def divide_number(number, chunk_size=10):
        divided_parts = []
        for i in range(0, len(number), chunk_size):
            divided_parts.append(number[i:i + chunk_size])
        return divided_parts

    @staticmethod
    def load_data_from_file(file_path: str) -> list:
        bank_data = []
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                bank_data.append(row[1])

        return bank_data

    @staticmethod
    def convert_str_to_num(iban: str):
        iban_numeric = ''
        for char in iban:
            if char.isdigit():
                iban_numeric += char
            else:
                iban_numeric += str(ord(char) - ord('A') + 10)

        return iban_numeric

    @staticmethod
    def calculate_reminder(iban_parts: list) -> int:
        last_reminder = None
        for part in iban_parts:
            number = str(last_reminder) + str(part) if last_reminder is not None else str(part)
            reminder = int(number) % 97
            last_reminder = reminder
        else:
            pre_reminder = last_reminder
            final_reminder = 98 - pre_reminder

        return final_reminder

    def create_default_iban(self, bank_num: str, account_num: str):
        return self.iban_prefix + bank_num + account_num

    def iban_checksum(self, iban):
        iban = iban[4:] + iban[:4]

        iban_numeric = self.convert_str_to_num(iban)

        iban_parts = self.divide_number(iban_numeric)
        reminder = self.calculate_reminder(iban_parts)
        answer = reminder

        if int(reminder) < 10:
            answer = f'0{reminder}'

        return str(answer)

    def generate_iban(self, records_to_generate: int) -> List[IBANModel]:
        response_data = []
        for i in range(0, records_to_generate):
            random_bank_num = random.choice(self.bank_institutions)

            iban_pl = self.create_default_iban(random_bank_num, self.generate_random_account_number())

            checksum = self.iban_checksum(iban_pl)
            checksum = f"PL{checksum}"

            result = iban_pl.replace(self.iban_prefix, checksum)

            iban = IBANModel(
                iban=result
            )
            response_data.append(iban)

        return response_data


iban_generator = IBANGenerator()

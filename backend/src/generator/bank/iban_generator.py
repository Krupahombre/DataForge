import logging
import random
import string


class IBANGenerator:
    def __init__(self):
        self.logger = logging.getLogger("IbanGenerator")
        self.iban_prefix = 'PL00'
        self.bank_num_length = 16

    def generate_random_account_number(self):
        return ''.join(random.choices(string.digits, k=self.bank_num_length))

    @staticmethod
    def divide_number(number, chunk_size=10):
        divided_parts = []
        for i in range(0, len(number), chunk_size):
            divided_parts.append(number[i:i + chunk_size])
        return divided_parts

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

    def generate_iban(self, bank_num: str) -> str:
        iban_pl = self.create_default_iban(bank_num, self.generate_random_account_number())

        checksum = self.iban_checksum(iban_pl)
        checksum = f"PL{checksum}"

        result = iban_pl.replace(self.iban_prefix, checksum)

        return result


iban_generator = IBANGenerator()

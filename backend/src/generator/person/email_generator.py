import logging
import random

from unidecode import unidecode

from src.database.generic_dal import get_all
from src.database.models.email_domains import EmailDomains


class EmailGenerator:
    def __init__(self):
        self.domains_file = 'data/email_domains.csv'
        self.domains = get_all(EmailDomains)

    @staticmethod
    def load_data_from_txt(file_path: str) -> list[str]:
        with open(file_path, 'r') as file:
            return file.readlines()

    @staticmethod
    def get_random_line(lines: list[str]):
        return random.choice(lines).strip()

    def generate_email(self, first_name: str, last_name: str) -> str:
        random_domain = random.choice(self.domains).domain
        f_name_decoded = unidecode(first_name).strip().replace(" ", "_").replace("-", "_").lower()
        l_name_decoded = unidecode(last_name).strip().replace(" ", "_").replace("-", "_").lower()

        return f'{f_name_decoded}.{l_name_decoded}@{random_domain}'


email_generator = EmailGenerator()

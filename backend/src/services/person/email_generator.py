import random

from unidecode import unidecode


class EmailGenerator:
    def __init__(self):
        self.domains_file = 'backend/data/all_email_provider_domains.txt'
        # self.domains_file = '/code/src/services/person/data/all_email_provider_domains.txt'
        self.domains = self.load_data_from_txt(self.domains_file)

    @staticmethod
    def load_data_from_txt(file_path: str) -> list[str]:
        with open(file_path, 'r') as file:
            return file.readlines()

    @staticmethod
    def get_random_line(lines: list[str]):
        return random.choice(lines).strip()

    def generate_email(self, first_name: str, last_name: str) -> str:
        random_domain = self.get_random_line(self.domains)
        f_name_decoded = unidecode(first_name).strip().replace(" ", "_").replace("-", "_").lower()
        l_name_decoded = unidecode(last_name).strip().replace(" ", "_").replace("-", "_").lower()

        return f'{f_name_decoded}.{l_name_decoded}@{random_domain}'


email_generator = EmailGenerator()

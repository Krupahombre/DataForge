import csv
import datetime
import random
from time import sleep

from unidecode import unidecode

from backend.src.services.base_generator import BaseGenerator


class PersonGenerator(BaseGenerator):
    def __init__(self):
        # self.domains = '/code/src/services/person/data/all_email_provider_domains.txt'
        # self.male_names = '/code/src/services/person/data/male_names.csv'
        # self.male_surnames = '/code/src/services/person/data/male_surnames.csv'
        self.domains = 'data/all_email_provider_domains.txt'
        self.male_names = 'data/male_names.csv'
        self.male_surnames = 'data/male_surnames.csv'
        self.supported_types = ["person"]

    def get_supported_types(self) -> list[str]:
        return self.supported_types

    def generate(self, types: list[str]) -> dict[str, any]:
        for type in types:
            if type not in self.supported_types:
                raise Exception(f"Unsupported type {type}")
        return dict([("person", self.generate_person())])

    @staticmethod
    def load_data_from_csv(file_path: str) -> list:
        data = []
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                data.append(row[0])

        return data

    @staticmethod
    def get_random_line_from_txt(file_path: str) -> str:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            return random.choice(lines).strip()

    @staticmethod
    def generate_birthdate():
        start_date = datetime.date(1950, 1, 1)
        end_date = datetime.date(2001, 12, 31)
        return start_date + datetime.timedelta(days=random.randint(0, (end_date - start_date).days))

    def generate_email(self, first_name: str, last_name: str):
        random_domain = self.get_random_line_from_txt(self.domains)
        f_name_decoded = unidecode(first_name).strip().replace(" ", "_").replace("-", "_").lower()
        l_name_decoded = unidecode(last_name).strip().replace(" ", "_").replace("-", "_").lower()
        return f'{f_name_decoded}.{l_name_decoded}@{random_domain}'

    def generate_person(self) -> str:
        male_names = self.load_data_from_csv(self.male_names)
        male_surnames = self.load_data_from_csv(self.male_surnames)

        first_name = random.choice(male_names)
        last_name = random.choice(male_surnames)
        birthdate = self.generate_birthdate().strftime("%Y-%m-%d")
        email = self.generate_email(first_name, last_name)

        person = f"{first_name.title()} {last_name.title()} {birthdate} {email}"

        return person


person_generator = PersonGenerator()

if __name__ == "__main__":
    while True:
        result = person_generator.generate_person()
        print(result)
        sleep(1)

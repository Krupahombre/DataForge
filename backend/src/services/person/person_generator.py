import csv
import datetime
import random

from src.services.base_generator import BaseGenerator


class PersonGenerator(BaseGenerator):
    def __init__(self):
        self.male_names = '/code/src/services/person/data/male_names.csv'
        self.male_surnames = '/code/src/services/person/data/male_surnames.csv'
        # self.male_names = 'data/male_names.csv'
        # self.male_surnames = 'data/male_surnames.csv'
        self.supported_types = ["person"]

    def get_supported_types(self) -> list[str]:
        return self.supported_types

    def generate(self, types: list[str]) -> dict[str, any]:
        for type in types:
            if type not in self.supported_types:
                raise Exception(f"Unsupported type {type}")
        return dict([("person", self.generate_person())])

    @staticmethod
    def load_data_from_file(file_path: str) -> list:
        data = []
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                data.append(row[0])

        return data

    @staticmethod
    def generate_birthdate():
        start_date = datetime.date(1950, 1, 1)
        end_date = datetime.date(2001, 12, 31)
        return start_date + datetime.timedelta(days=random.randint(0, (end_date - start_date).days))

    @staticmethod
    def generate_email(first_name: str):
        pass

    def generate_person(self) -> str:
        male_names = self.load_data_from_file(self.male_names)
        male_surnames = self.load_data_from_file(self.male_surnames)

        first_name = random.choice(male_names)
        last_name = random.choice(male_surnames)
        birthdate = self.generate_birthdate().strftime("%Y-%m-%d")

        person = f"{first_name.capitalize()} {last_name.capitalize()} {birthdate.capitalize()}"

        return person


person_generator = PersonGenerator()

# if __name__ == "__main__":
#     result = person_generator.generate_person()
#     print(result)

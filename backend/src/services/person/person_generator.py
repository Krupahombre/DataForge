import csv
import datetime
import random
from time import sleep
from typing import Tuple

from pydantic import BaseModel
from src.services.base_generator import BaseGenerator
from src.services.person.email_generator import email_generator
from src.services.person.pesel_generator import pesel_generator
from src.utils.enums.gender import GenderEnum


class PersonModel(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    sex: str | None = None
    birthday: str | None = None
    pesel: int | None = None
    email: str | None = None


class PersonGenerator(BaseGenerator):
    def __init__(self):
        self.male_names_file_path = '/code/src/services/person/data/male_names.csv'
        self.male_surnames_file_path = '/code/src/services/person/data/male_surnames.csv'
        self.female_names_file_path = '/code/src/services/person/data/female_names.csv'
        self.female_surnames_file_path = '/code/src/services/person/data/female_surnames.csv'
        # self.male_names_file_path = 'data/male_names.csv'
        # self.male_surnames_file_path = 'data/male_surnames.csv'
        # self.female_names_file_path = 'data/female_names.csv'
        # self.female_surnames_file_path = 'data/female_surnames.csv'
        self.supported_types = ["person"]

    def get_supported_types(self) -> list[str]:
        return self.supported_types

    def generate(self, types: list[str]) -> dict[str, any]:
        for type in types:
            if type not in self.supported_types:
                raise Exception(f"Unsupported type {type}")
        return dict([("person", self.generate_person())])

    @staticmethod
    def select_random_sex() -> str:
        return random.choice(list(GenderEnum)).name.lower()

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
    def generate_birthdate() -> datetime:
        start_date = datetime.date(1950, 1, 1)
        end_date = datetime.date(2001, 12, 31)
        return start_date + datetime.timedelta(days=random.randint(0, (end_date - start_date).days))

    def get_data_by_gender(self, gender: str) -> Tuple[str, str]:
        if gender == GenderEnum.MALE.name.lower():
            return self.male_names_file_path, self.male_surnames_file_path
        elif gender == GenderEnum.FEMALE.name.lower():
            return self.female_names_file_path, self.female_surnames_file_path

    def generate_person(self) -> str:
        sex_choice = self.select_random_sex()

        names_file_choice, surnames_file_choice = self.get_data_by_gender(sex_choice)

        names_list = self.load_data_from_csv(names_file_choice)
        surnames_list = self.load_data_from_csv(surnames_file_choice)

        first_name = random.choice(names_list)
        last_name = random.choice(surnames_list)
        sex = sex_choice
        birthdate = self.generate_birthdate()
        pesel = pesel_generator.generate_pesel(birthdate, sex)
        email = email_generator.generate_email(first_name, last_name)

        person = PersonModel(
            first_name=first_name.title(),
            last_name=last_name.title(),
            sex=sex,
            birthday=birthdate.strftime('%Y-%m-%d'),
            pesel=pesel,
            email=email
        )
        # person = f"{first_name.title()} {last_name.title()} {sex} {birthdate.strftime('%Y-%m-%d')} {pesel} {email}"

        return person.model_dump_json()


person_generator = PersonGenerator()


if __name__ == "__main__":
    while True:
        result = person_generator.generate_person()
        print(result)
        sleep(1)

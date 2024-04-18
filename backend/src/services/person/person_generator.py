import csv
import datetime
import logging
import random
from time import sleep
from typing import Tuple, List

from pydantic import BaseModel
from backend.src.services.base_generator import BaseGenerator
from backend.src.services.person.email_generator import email_generator
from backend.src.services.person.pesel_generator import pesel_generator
from backend.src.utils.enums.gender import GenderEnum

logger = logging.getLogger("PersonGenerator")


class PersonModel(BaseModel):
    first_name: str = None
    last_name: str = None
    sex: str = None
    birthday: str = None
    pesel: int = None
    email: str = None


class PersonGenerator(BaseGenerator):
    def __init__(self):
        # self.male_names_file_path = '/code/src/services/person/data/male_names.csv'
        #
        # self.male_surnames_file_path = '/code/src/services/person/data/male_surnames.csv'
        # self.female_names_file_path = '/code/src/services/person/data/female_names.csv'
        # self.female_surnames_file_path = '/code/src/services/person/data/female_surnames.csv'
        self.male_names_file_path = './backend/data/male_names.csv'
        self.male_surnames_file_path = './backend/data/male_surnames.csv'
        self.female_names_file_path = './backend/data/female_names.csv'
        self.female_surnames_file_path = './backend/data/female_surnames.csv'
        self.males = (
            self.load_data_from_csv(self.male_names_file_path),
            self.load_data_from_csv(self.male_surnames_file_path)
        )
        self.females = (
            self.load_data_from_csv(self.female_names_file_path),
            self.load_data_from_csv(self.female_surnames_file_path)
        )
        self.supported_types = ["person"]

    def get_supported_types(self) -> list[str]:
        return self.supported_types

    def generate(self, types: list[str], records_to_generate: int) -> dict[str, any]:
        for type in types:
            if type not in self.supported_types:
                logger.exception(f"Unsupported data type: {type}")
                raise Exception(f"Unsupported type {type}")
        return dict([("person", self.generate_person(records_to_generate))])

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

    def get_data_by_gender(self, gender: str) -> Tuple[list[str], list[str]]:
        if gender == GenderEnum.MALE.name.lower():
            return self.males
        elif gender == GenderEnum.FEMALE.name.lower():
            return self.females

    def generate_person(self, records_to_generate: int) -> List[PersonModel]:
        response_data = []
        for i in range(0, records_to_generate):
            sex_choice = self.select_random_sex()
            names, surnames = self.get_data_by_gender(sex_choice)
            first_name = random.choice(names)
            last_name = random.choice(surnames)
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
            response_data.append(person)
        # person = f"{first_name.title()} {last_name.title()} {sex} {birthdate.strftime('%Y-%m-%d')} {pesel} {email}"

        return response_data


person_generator = PersonGenerator()

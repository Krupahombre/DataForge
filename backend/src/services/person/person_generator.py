import csv
import datetime
import random
from enum import Enum
from time import sleep

from unidecode import unidecode

from backend.src.services.base_generator import BaseGenerator


class SexEnum(Enum):
    MALE = 0
    FEMALE = 1


class PersonGenerator(BaseGenerator):
    def __init__(self):
        # self.domains = '/code/src/services/person/data/all_email_provider_domains.txt'
        # self.male_names = '/code/src/services/person/data/male_names.csv'
        # self.male_surnames = '/code/src/services/person/data/male_surnames.csv'
        self.domains = 'data/all_email_provider_domains.txt'
        self.male_names = 'data/male_names.csv'
        self.male_surnames = 'data/male_surnames.csv'
        self.female_names = 'data/female_names.csv'
        self.female_surnames = 'data/female_surnames.csv'
        self.control_digit_weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
        self.pesel_male_digits = [1, 3, 5, 7, 9]
        self.pesel_female_digits = [0, 2, 4, 6, 8]
        self.supported_types = ["person"]
        super().__init__()

    def get_supported_types(self) -> list[str]:
        return self.supported_types

    def generate(self, types: list[str]) -> dict[str, any]:
        for sup_type in types:
            if sup_type not in self.supported_types:
                raise Exception(f"Unsupported type {sup_type}")
        return dict([("person", self.generate_person())])

    @staticmethod
    def select_random_sex():
        return random.choice(list(SexEnum)).name.lower()

    def calculate_control_digit(self, pre_pesel: str) -> str:
        sum = 0
        for i in range(len(pre_pesel)):
            result = int(pre_pesel[i]) * self.control_digit_weights[i]
            if result >= 10:
                result = result % 10

            sum += result

        if sum >= 10:
            sum = sum % 10
        control_digit = (10 - sum) % 10

        return str(control_digit)

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

    @staticmethod
    def get_century_code(year: int) -> int:
        century_code = 0
        if 1800 <= year <= 1899:
            century_code = 80
        elif 1900 <= year <= 1999:
            century_code = 0
        elif 2000 <= year <= 2099:
            century_code = 20

        return century_code

    def generate_pesel(self, birth_date, gender_weights_digits):
        year = birth_date.year % 100
        month = birth_date.month
        day = birth_date.day

        century_code = self.get_century_code(birth_date.year)

        month += century_code

        birth_date_str = f"{year:02}{month:02}{day:02}"

        order_number = random.randint(100, 999)
        order_number_str = f"{order_number:03}"

        sex_number = random.choice(gender_weights_digits)
        sex_number_str = f"{sex_number:01}"

        pre_pesel = birth_date_str + order_number_str + sex_number_str

        control_digit = self.calculate_control_digit(pre_pesel)

        pesel = birth_date_str + order_number_str + sex_number_str + control_digit

        return pesel

    def get_data_by_gender(self, gender: str):
        if gender == SexEnum.MALE.name.lower():
            return self.male_names, self.male_surnames, self.pesel_male_digits
        elif gender == SexEnum.FEMALE.name.lower():
            return self.female_names, self.female_surnames, self.pesel_female_digits

    def generate_person(self) -> str:
        sex_choice = self.select_random_sex()

        names_file_choice, surnames_file_choice, pesel_gender_digits_choice = self.get_data_by_gender(sex_choice)

        names_list = self.load_data_from_csv(names_file_choice)
        surnames_list = self.load_data_from_csv(surnames_file_choice)

        first_name = random.choice(names_list)
        last_name = random.choice(surnames_list)
        sex = sex_choice
        birthdate = self.generate_birthdate()
        pesel = self.generate_pesel(birthdate, pesel_gender_digits_choice)
        email = self.generate_email(first_name, last_name)

        person = f"{first_name.title()} {last_name.title()} {sex} {birthdate.strftime('%Y-%m-%d')} {pesel} {email}"

        return person


person_generator = PersonGenerator()


if __name__ == "__main__":
    while True:
        result = person_generator.generate_person()
        print(result)
        sleep(1)

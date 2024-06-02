import random
from datetime import datetime

from src.utils.enums.gender import GenderEnum


class PeselGenerator:
    def __init__(self):
        self.control_digit_weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
        self.pesel_male_digits = [1, 3, 5, 7, 9]
        self.pesel_female_digits = [0, 2, 4, 6, 8]

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

    def get_weight_digits_by_gender(self, gender: str) -> list:
        return self.pesel_male_digits if gender == GenderEnum.MALE.name.lower() else self.pesel_female_digits

    def generate_pesel(self, birth_date: datetime, gender: str) -> str:
        year = birth_date.year % 100
        month = birth_date.month
        day = birth_date.day

        century_code = self.get_century_code(birth_date.year)

        month += century_code

        birth_date_str = f"{year:02}{month:02}{day:02}"

        order_number = random.randint(100, 999)
        order_number_str = f"{order_number:03}"

        gender_weights_digits = self.get_weight_digits_by_gender(gender)

        sex_number = random.choice(gender_weights_digits)
        sex_number_str = f"{sex_number:01}"

        pre_pesel = birth_date_str + order_number_str + sex_number_str

        control_digit = self.calculate_control_digit(pre_pesel)

        pesel = birth_date_str + order_number_str + sex_number_str + control_digit

        return pesel


pesel_generator = PeselGenerator()

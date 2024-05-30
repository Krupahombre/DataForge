import datetime
import logging
import random

from pydantic import BaseModel

from src.database.generic_dal import get_all
from src.database.models.female_last_names import FemaleLastNames
from src.database.models.female_names import FemaleNames
from src.database.models.male_last_names import MaleLastNames
from src.database.models.male_names import MaleNames
from src.generator.base_generator import BaseGenerator
from src.generator.person.email_generator import email_generator
from src.generator.person.pesel_generator import pesel_generator
from src.utils.enums.gender import GenderEnum
from nickname_generator import generate

logger = logging.getLogger("PersonGenerator")
fields = ["name", "last_name", "sex", "birth_date", "pesel", "email"]


class PersonModel(BaseModel):
    first_name: str = None
    last_name: str = None
    sex: str = None
    birthday: str = None
    pesel: int = None
    email: str = None


class PersonGenerator(BaseGenerator):
    def __init__(self):
        super().__init__()
        self.male_names = get_all(MaleNames)
        self.male_last_names = get_all(MaleLastNames)
        self.female_names = get_all(FemaleNames)
        self.female_last_names = get_all(FemaleLastNames)
        self.supported_types = ["person"]

    def get_supported_types(self) -> list[str]:
        return self.supported_types

    @staticmethod
    def get_fields() -> list[str]:
        return fields

    def get_name(self) -> str:
        return "person"

    def generate(self, field: str, records_to_generate: int, seed_list: list = None, metadata: list = None) -> list:
        if field not in fields:
            logger.exception(f"Unsupported field {field}")
            raise Exception(f"Unsupported field {field}")
        match field:
            case "name":
                return self.generate_name_or_last_name(metadata, records_to_generate, field)
            case "last_name":
                return self.generate_name_or_last_name(metadata, records_to_generate, field)
            case "sex":
                return self.generate_sex(records_to_generate)
            case "birth_date":
                return self.generate_birthdate(records_to_generate)
            case "pesel":
                return self.generate_pesel(metadata, records_to_generate)
            case "email":
                return self.generate_email(metadata, records_to_generate)

    @staticmethod
    def select_random_sex() -> str:
        return random.choice(list(GenderEnum)).name.lower()

    @staticmethod
    def generate_birthdate(records_to_generate: int) -> list:
        out = []
        for i in range(0, records_to_generate):
            start_date = datetime.date(1950, 1, 1)
            end_date = datetime.date(2001, 12, 31)
            out.append(start_date + datetime.timedelta(days=random.randint(0, (end_date - start_date).days)))
        return out

    def generate_sex(self, records_to_generate: int) -> list:
        out = []
        for i in range(0, records_to_generate):
            out.append(self.select_random_sex())
        return out

    def generate_name_or_last_name(self, metadata: list, records_to_generate: int, type: str) -> list:
        out = []
        sexes = metadata[0] if metadata else None
        for i in range(0, records_to_generate):
            if sexes:
                sex = sexes[i]
            else:
                sex = random.choice(list(GenderEnum)).name.lower()

            if sex == 'male':
                out.append(random.choice(self.male_names if type == "name" else self.male_last_names).name)
            else:
                out.append(random.choice(self.female_names if type == "name" else self.female_last_names).name)
        return out

    @staticmethod
    def generate_pesel(metadata: list, records_to_generate: int) -> list:
        args_num = len(metadata)
        sexes = metadata[0] if args_num >= 2 else None
        if args_num >= 2:
            birthdates = metadata[1]
        elif args_num == 1:
            birthdates = metadata[0]
        else:
            birthdates = None

        out = []
        for i in range(0, records_to_generate):
            if sexes:
                sex = sexes[i]
            else:
                sex = random.choice(list(GenderEnum)).name.lower()

            if birthdates:
                birthdate = birthdates[i]
            else:
                birthdate = PersonGenerator.generate_birthdate(1)[0]

            out.append(pesel_generator.generate_pesel(birthdate, sex))
        return out

    @staticmethod
    def generate_email(metadata: list, records_to_generate: int) -> list:
        args_num = len(metadata)
        first_names = metadata[0] if args_num >= 1 else None
        last_names = metadata[1] if args_num >= 2 else None
        out = []
        for i in range(0, records_to_generate):
            if first_names and last_names:
                out.append(email_generator.generate_email(first_names[i], last_names[i]))
            else:
                out.append(email_generator.generate_email(generate(), generate()))
        return out


person_generator = PersonGenerator()

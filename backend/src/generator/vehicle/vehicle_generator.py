import json
import logging
import os
import random
import string
import subprocess

from src.generator.base_generator import BaseGenerator

logger = logging.getLogger("VehicleGenerator")
fields = ["make", "model", "year", "body_type", "drivetrain", "engine_type", "exterior_colors", "interior_colors", "vin"]


class VehicleDataGenerator(BaseGenerator):
    def __init__(self):
        super().__init__()
        self.characters = string.digits + string.ascii_letters
        self.default_file_name = "vehicle-data-"
        self.script_command = "ruby vehicle_data.rb {records_to_generate} {file_name}"
        self.supported_types = ["vehicle"]

    def get_supported_types(self) -> list[str]:
        return self.supported_types

    @staticmethod
    def get_fields() -> list[str]:
        return fields

    @staticmethod
    def get_name() -> str:
        return "vehicle"

    @staticmethod
    def replace_placeholders(command: str, records_to_generate: int, file_name: str) -> str:
        return (command
                .replace("{records_to_generate}", str(records_to_generate))
                .replace("{file_name}", file_name))

    @staticmethod
    def read_data_file(file_path: str):
        with open(file_path, "r") as file:
            file_content = file.read()
        return json.loads(file_content)

    @staticmethod
    def delete_data_file(file_path: str) -> None:
        os.remove(file_path)

    def create_file_name(self) -> str:
        random_signs = ''.join(random.choices(self.characters, k=5))
        return self.default_file_name + random_signs + '.json'

    def generate_subset(self, field: str, records_to_generate: int, seed_list: list = None, metadata: list = None) -> list:
        file_name = self.create_file_name()
        file_path = "./" + file_name
        command_to_execute = self.replace_placeholders(self.script_command, records_to_generate, file_name)

        process = subprocess.Popen(
            command_to_execute.split(),
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        ).wait()

        result = self.read_data_file(file_path)
        self.delete_data_file(file_path)

        return result


vehicle_data_generator = VehicleDataGenerator()

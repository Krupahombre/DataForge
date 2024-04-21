class BaseGenerator:
    def __init__(self):
        self.supported_types = []

    def get_supported_data(self) -> list[str]:
        pass

    def generate(self, types: list[str], records_to_generate: int) -> dict[str, any]:
        pass

    def check_support(self, types: list[str]):
        pass

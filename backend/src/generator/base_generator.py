class BaseGenerator:
    def __init__(self):
        self.supported_types = []

    def get_supported_types(self) -> list[str]:
        pass

    @staticmethod
    def get_fields() -> list[str]:
        pass

    def get_name(self) -> str:
        pass

    def generate(self, field: str, records: int, seed_list: list = None, metadata: list = None) -> list:
        pass

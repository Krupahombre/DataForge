from src.services.data_generator_service import generate_data


def generate_data_with_response_format(generators_list: list[str]):
    result_data = generate_data(generators_list)

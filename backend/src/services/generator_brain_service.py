from src.services.data_generator_service import generate_data

from src.services.query_generator_service import generate_sql_query

from src.server.models.generator_model import GeneratorModel


def generate_data_with_response_format(generators_list: GeneratorModel):
    result_data = generate_data(generators_list)

    result_query = generate_sql_query(result_data)

    return result_query

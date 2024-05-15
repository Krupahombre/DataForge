import logging
from datetime import datetime

from src.services.data_generator_service import generate_data

from src.services.query_generator_service import generate_sql_query

from src.server.models.generator_model import GeneratorModel

logger = logging.getLogger("GeneratorBrainService")


def generate_data_with_response_format(params: GeneratorModel):
    start_time = datetime.now()
    logger.info(f"Generating query for {params.records} records and generator list: {params.tables}...")
    result_data = generate_data(params)
    result_query = generate_sql_query(result_data)
    logger.info(f"End query generated in {datetime.now() - start_time}[s]")
    return result_query

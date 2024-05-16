import logging
from datetime import datetime

from fastapi import HTTPException
from starlette import status

from src.services.data_generator_service import generate_data

from src.services.query_generator_service import generate_sql_query

from src.server.models.generator_model import GeneratorModel
from src.utils.enums.response_format import ResponseFormat

logger = logging.getLogger("GeneratorBrainService")


def generate_data_with_response_format(params: GeneratorModel):
    start_time = datetime.now()
    logger.info(f"Generating response for {params.records} records and generator list: {params.tables}...")
    result_data = generate_data(params)
    if params.format == ResponseFormat.POSTGRESQL or params.format == ResponseFormat.MYSQL:
        result_query = generate_sql_query(result_data, params.records, params.format)
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Unsupported response format: {params.format}"
        )
    logger.info(f"Response generated in {datetime.now() - start_time}[s]")
    return result_query

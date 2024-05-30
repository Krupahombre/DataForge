import logging
from datetime import datetime

from fastapi import HTTPException
from starlette import status

from src.services.data_generator_service import generate_data
from src.services.json_generator_service import generate_json

from src.services.query_generator_service import generate_sql_query

from src.server.models.generator_model import GeneratorModel, Table
from src.utils.enums.response_format import ResponseFormat

logger = logging.getLogger("GeneratorBrainService")


def generate_data_with_response_format(params: GeneratorModel):
    start_time = datetime.now()
    if not valid_tables(params.tables):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid table configuration: name repetition within columns"
        )
    logger.info(f"Generating response for {params.records} records and generator list: {params.tables}...")
    result_data = generate_data(params)
    if params.format == ResponseFormat.POSTGRESQL or params.format == ResponseFormat.MYSQL:
        result_query = generate_sql_query(result_data, params.records, params.format)
    elif params.format == ResponseFormat.JSON:
        result_query = generate_json(result_data, params.records, params.format)
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Unsupported response format: {params.format}"
        )
    logger.info(f"Response generated in {datetime.now() - start_time}[s]")
    return result_query


def valid_tables(tables: list[Table]):
    for table in tables:
        fields = set([field.name for field in table.fields])
        if len(fields) != len(table.fields):
            return False
    return True

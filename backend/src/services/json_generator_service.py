import datetime
import logging

from fastapi import HTTPException
from starlette import status

from src.generator import FIELD_TYPES
from src.utils.enums.response_format import ResponseFormat
from src.utils.enums.sql_templates import PostgreSQLTemplates, MySQLTemplates

logger = logging.getLogger("QueryGeneratorService")


def generate_json(result: dict, records_num: int, type: ResponseFormat) -> dict[str, str]:
    if type != ResponseFormat.JSON:
        logger.exception(f"Invalid response format for json: {type}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Invalid format for json: {type}"
        )
    output = {}
    for table in result:
        id_holder = 1
        result_gen = result[table]
        objects = []
        for i in range(0, records_num):
            obj = {"id": id_holder}
            for element in result_gen:
                value = result_gen[element][i]
                obj[element[0]] = value
            objects.append(obj)
            id_holder += 1
        output[table] = objects
    return output

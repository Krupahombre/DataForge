import logging

from fastapi import HTTPException
from starlette import status

from src.utils.enums.response_format import ResponseFormat

logger = logging.getLogger("QueryGeneratorService")


def generate_csv(result: dict, records_num: int, type: ResponseFormat) -> dict[str, str]:
    if type != ResponseFormat.CSV:
        logger.exception(f"Invalid response format for csv: {type}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Invalid format for json: {type}"
        )
    output = {}
    for table in result:
        id_holder = 1
        result_gen = result[table]
        table_str = 'id, '
        for element in result_gen:
            table_str += element[0] + ', '
        table_str = table_str[:-2]
        table_str += '\n'
        for i in range(0, records_num):
            table_str += str(id_holder) + ', '
            for element in result_gen:
                value = result_gen[element][i]
                table_str += str(value) + ', '
            id_holder += 1
            table_str = table_str[:-2]
            table_str += '\n'
        output[table] = table_str
    return output

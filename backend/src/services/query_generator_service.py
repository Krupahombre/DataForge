import datetime
import logging

from fastapi import HTTPException
from starlette import status

from src.generator import FIELD_TYPES
from src.utils.enums.response_format import ResponseFormat
from src.utils.enums.sql_templates import PostgreSQLTemplates, MySQLTemplates

logger = logging.getLogger("QueryGeneratorService")


def generate_sql_query(result: dict, records_num: int, type: ResponseFormat) -> dict[str, str]:
    final_queries: dict[str, str] = {}
    if type != ResponseFormat.POSTGRESQL and type != ResponseFormat.MYSQL:
        logger.exception(f"Invalid response format for sql query: {type}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Invalid format for sql query: {type}"
        )
    template = PostgreSQLTemplates if type == ResponseFormat.POSTGRESQL else MySQLTemplates
    for table in result:
        result_gen = result[table]
        table_name = table
        definitions = []
        inserts = []
        final_inserts = []
        columns = []
        
        for key, values in result_gen.items():
            column_name = key[0]
            field_space, field_name = key[1].split(':')
            field_type = FIELD_TYPES[field_space][field_name]

            if field_type == str or field_type == datetime.date:
                key_type = template.VARCHAR_TYPE.value.replace('{column_name}', column_name)
            elif field_type == int:
                key_type = template.INT_TYPE.value.replace('{column_name}', column_name)
            else:
                logger.exception(f"Unsupported field type: {field_type}")
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail=f"Unsupported field type: {field_type}"
                )
            if template == PostgreSQLTemplates:
                column_name = '"' + key[0] + '"'
            elif template == MySQLTemplates:
                column_name = '`' + key[0] + '`'
            columns.append(column_name)
            definitions.append(key_type)
        definitions_str = '+'.join(definitions).replace('+', ', ')
        columns_str = '+'.join(columns).replace('+', ', ')

        for i in range(0, records_num):
            for element in result_gen:
                value = result_gen[element][i]
                field_space, field_name = element[1].split(':')
                field_type = FIELD_TYPES[field_space][field_name]

                if field_type == str:
                    insert_str_pre = "'" + str(value) + "'"
                    inserts.append(insert_str_pre)
                elif field_type == int:
                    inserts.append(str(value))
            inserts_str = '+'.join(inserts).replace('+', ', ')
            final_inserts.append(str('(' + inserts_str + ')'))
            del inserts
            inserts = []

        drop_table_command = template.DROP_TABLE_IF_EXIST.value.replace('{table_name}', table_name)

        create_table_command = (
            template.CREATE_TABLE.value
            .replace('{table_name}', table_name)
            .replace('{definitions}', definitions_str)
        )

        inserts_to_query = ', '.join(final_inserts)
        insert_into_command = (
            template.INSERT_INTO.value
            .replace('{table_name}', table_name)
            .replace('{columns}', columns_str)
            .replace('{inserts}', inserts_to_query)
        )

        final_query_gen = ' '.join([drop_table_command, create_table_command, insert_into_command])
        final_queries[table] = final_query_gen
    return final_queries

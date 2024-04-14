from typing import List

from src.utils.enums.sql_templates import PostgreSQLTemplates
from src.utils.field_type_getter import get_field_type


def generate_sql_query(result: dict) -> List[str]:
    final_queries = []

    for generator in result:
        result_gen = result[generator]

        table_name = generator
        definitions = []
        inserts = []
        final_inserts = []
        columns = []
        
        for key, value in result_gen[0].dict().items():
            column_name = key
            field_type = get_field_type(result_gen[0].__class__, key)

            if field_type == str:
                key_type = PostgreSQLTemplates.VARCHAR_TYPE.value.replace('{column_name}', column_name)
            elif field_type == int:
                key_type = PostgreSQLTemplates.INT_TYPE.value.replace('{column_name}', column_name)
            else:
                raise Exception("Unsupported field type")

            columns.append(column_name)
            definitions.append(key_type)

        for element in result_gen:
            for key, value in element.dict().items():
                if value is not None:
                    field_type = get_field_type(element.__class__, key)

                    if field_type == str:
                        insert_str_pre = "'" + str(value) + "'"
                        inserts.append(insert_str_pre)
                    elif field_type == int:
                        inserts.append(str(value))

            definitions_str = '+'.join(definitions).replace('+', ', ')
            columns_str = '+'.join(columns).replace('+', ', ')
            inserts_str = '+'.join(inserts).replace('+', ', ')

            final_inserts.append(str('(' + inserts_str + ')'))

            del inserts
            inserts = []

        drop_table_command = PostgreSQLTemplates.DROP_TABLE_IF_EXIST.value.replace('{table_name}', table_name)

        create_table_command = (
            PostgreSQLTemplates.CREATE_TABLE.value
            .replace('{table_name}', table_name)
            .replace('{definitions}', definitions_str)
        )

        inserts_to_query = ', '.join(final_inserts)
        insert_into_command = (
            PostgreSQLTemplates.INSERT_INTO.value
            .replace('{table_name}', table_name)
            .replace('{columns}', columns_str)
            .replace('{inserts}', inserts_to_query)
        )

        final_query_gen = ' '.join([drop_table_command, create_table_command, insert_into_command])
        final_queries.append(final_query_gen)

        print(f"Query assembled successfully for {generator} generator")

    return final_queries

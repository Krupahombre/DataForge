from enum import Enum


class SQLTemplates(Enum):
    DROP_TABLE_IF_EXIST = 'DROP TABLE IF EXISTS "{table_name}";'
    CREATE_TABLE = 'CREATE TABLE "{table_name}" ( {table_name}_id SERIAL PRIMARY KEY, {definitions} );'
    INSERT_INTO = 'INSERT INTO "{table_name}" ({columns}) VALUES {INSERTS};'
    VARCHAR_TYPE = '{column_name} VARCHAR(255)'
    INT_TYPE = '{column_name} INT'

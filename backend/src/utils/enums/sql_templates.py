from enum import Enum


class PostgreSQLTemplates(Enum):
    DROP_TABLE_IF_EXIST = 'DROP TABLE IF EXISTS "{table_name}";'
    CREATE_TABLE = 'CREATE TABLE "{table_name}" ({table_name}_id SERIAL PRIMARY KEY, {definitions});'
    INSERT_INTO = 'INSERT INTO "{table_name}" ({columns}) VALUES {inserts};'
    VARCHAR_TYPE = '{column_name} VARCHAR(255) NOT NULL'
    INT_TYPE = '{column_name} INTEGER NOT NULL'


class MySQLTemplates(Enum):
    DROP_TABLE_IF_EXIST = 'DROP TABLE IF EXISTS `{table_name}`;'
    CREATE_TABLE = ('CREATE TABLE `{table_name}` ({table_name}_id mediumint(8) unsigned NOT NULL auto_increment, '
                    '{definitions},'
                    'PRIMARY KEY (`{table_name}_id`)'
                    ') AUTO_INCREMENT=1;')
    INSERT_INTO = 'INSERT INTO `{table_name}` ({columns}) VALUES {inserts};'
    VARCHAR_TYPE = '`{column_name}` VARCHAR(255) NOT NULL'
    INT_TYPE = '`{column_name}` INTEGER NOT NULL'

from enum import Enum


class ResponseFormat(Enum):
    POSTGRESQL = 'psql'
    MYSQL = 'mysql'
    JSON = 'json'
    CSV = 'csv'

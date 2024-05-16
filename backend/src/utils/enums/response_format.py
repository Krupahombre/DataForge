from enum import Enum


class ResponseFormat(Enum):
    POSTGRESQL = 'postgresql'
    MYSQL = 'mysql'
    JSON = 'json'
    CSV = 'csv'

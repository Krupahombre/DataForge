import logging
from time import sleep

from src.utils.config_parser import parser
from playhouse.postgres_ext import PostgresqlExtDatabase


class DatabaseProvider:
    def __init__(self):
        self.logger = logging.getLogger("DatabaseProvider")
        self.is_connected = False
        self.db_name = parser.get_attr("database", "db_name")
        self.db_user = parser.get_attr("database", "user")
        self.db_password = parser.get_attr("database", "password")
        self.db_host = parser.get_attr("database", "host")
        self.db_port = parser.get_attr("database", "port")
        self.connect_attempts = int(parser.get_attr("database", "connect_attempts"))
        self.db = PostgresqlExtDatabase(database=self.db_name, user=self.db_user, password=self.db_password,
                                        host=self.db_host, port=self.db_port, autorollback=True)
        self.logger.info("Initializing connection to database")
        self.__connect()

    def __connect(self) -> None:
        for i in range(self.connect_attempts):
            sleep(1 * i)
            try:
                self.db.connect()
                self.is_connected = True
                self.logger.info("Connection to database established")
                return
            except Exception as e:
                self.logger.error(f"Connection to database failed. Attempt {i + 1}/{self.connect_attempts}")
                self.logger.error(e)
                self.is_connected = False
        if not self.is_connected:
            self.logger.error("Connection to database failed. Exiting...")
            exit(1)

    def close_connection(self):
        self.db.close()
        self.is_connected = False
        self.logger.info("Connection to database closed")


db_provider = DatabaseProvider()

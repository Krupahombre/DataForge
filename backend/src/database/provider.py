import logging
import os
from time import sleep

from playhouse.postgres_ext import PostgresqlExtDatabase
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class DatabaseProvider:
    def __init__(self):
        self.logger = logging.getLogger("DatabaseProvider")
        self.is_connected = False
        self.db_name = os.getenv("POSTGRES_DB")
        self.db_user = os.getenv("POSTGRES_USER")
        self.db_password = os.getenv("POSTGRES_PASSWORD")
        self.db_host = os.getenv("POSTGRES_HOST")
        self.db_port = os.getenv("POSTGRES_PORT")
        self.connect_attempts = 5
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

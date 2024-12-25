import pymysql
from pymysql.cursors import DictCursor


class SyncDBConnection:
    def __init__(self, db_config: dict):
        self.db_config = db_config
        self.connection = None

    def init_connection(self):
        """Initialize the database connection."""
        self.connection = pymysql.connect(
            host=self.db_config["host"],
            user=self.db_config["user"],
            password=self.db_config["password"],
            database=self.db_config["database"],
            cursorclass=DictCursor
        )

    def get_connection(self):
        """Get a connection."""

        if not self.connection:
            try:
                self.init_connection()
            except Exception as e:
                raise Exception(e)
        return self.connection

    def close_connection(self):
        """Close the connection."""
        if self.connection:
            self.connection.close()

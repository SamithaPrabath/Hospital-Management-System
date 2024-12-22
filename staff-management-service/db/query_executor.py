from db.db_connection import SyncDBConnection

class SyncQueryExecutor:
    def __init__(self, db_config):
        self.db_connection = SyncDBConnection(db_config)
        self.db_connection.init_connection()

    def execute(self, query, params=None):
        """Execute a query without returning results (e.g., INSERT, UPDATE, DELETE)."""
        conn = self.db_connection.get_connection()
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            conn.commit()

    def fetch_one(self, query, params=None):
        """Fetch one result from the database."""
        conn = self.db_connection.get_connection()
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            result = cursor.fetchone()
        return result

    def fetch_all(self, query, params=None):
        """Fetch all results from the database."""
        conn = self.db_connection.get_connection()
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            result = cursor.fetchall()
        return result

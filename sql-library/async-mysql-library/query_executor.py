from db_connection import AsyncDBConnection


class AsyncQueryExecutor:
    def __init__(self, db_config):
        self.db_config = db_config
        self.db_connection = AsyncDBConnection(db_config)

    async def execute(self, query):
        """Execute a query without returning results (e.g., INSERT, UPDATE, DELETE)."""
        conn = await self.db_connection.get_connection()
        async with conn.cursor() as cursor:
            await cursor.execute(query)
        await self.db_connection.release_connection(conn)

    async def fetch_one(self, query):
        """Fetch one result from the database."""
        conn = await self.db_connection.get_connection()
        async with conn.cursor() as cursor:
            await cursor.execute(query)
            result = await cursor.fetchone()
        await self.db_connection.release_connection(conn)
        return result

    async def fetch_all(self, query):
        """Fetch all results from the database."""
        conn = await self.db_connection.get_connection()
        async with conn.cursor() as cursor:
            await cursor.execute(query)
            result = await cursor.fetchall()
        await self.db_connection.release_connection(conn)
        return result

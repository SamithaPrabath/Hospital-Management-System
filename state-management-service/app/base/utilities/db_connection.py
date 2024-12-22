import aiomysql


class AsyncDBConnection:
    def __init__(self, db_config: dict) -> None:
        """
        Constructor for the AsyncDBConnection class.

        :param db_config:  dict  - A dictionary containing the database connection configuration.
            ex - {
                    "host": "localhost",
                    "port": 3306,
                    "user": "my-sql-user-name",
                    "password": "my-sql-password",
                    "database": "my-database-name"
                }

        :return: None
        """
        self.db_config = db_config
        self.pool = None

    async def init_pool(self) -> None:
        """Initialize the connection pool."""
        self.pool = await aiomysql.create_pool(
            host=self.db_config["host"],
            port=self.db_config["port"],
            user=self.db_config["user"],
            password=self.db_config["password"],
            db=self.db_config["database"],
            autocommit=True
        )

    async def get_connection(self) -> aiomysql.Connection:
        """Get a connection from the pool."""
        if self.pool:
            return await self.pool.acquire()
        elif not self.pool:
            await self.init_pool()
            return await self.pool.acquire()
        else:
            raise Exception("Connection pool not initialized.")

    async def release_connection(self, conn) -> None:
        """Release the connection back to the pool."""
        if self.pool:
            self.pool.release(conn)

    async def close_pool(self) -> None:
        """Close all connections in the pool."""
        if self.pool:
            self.pool.close()
            await self.pool.wait_closed()

import os

DB_USER: str = os.getenv('DB_USER', 'root')
DB_PASSWORD: str = os.getenv('DB_PASSWORD', '')
DB_NAME: str = os.getenv('DB_NAME', '')
DB_PORT: int = int(os.getenv('DB_PORT', '3306'))
DB_HOST: str = os.getenv('DB_HOST', '127.0.0.1')

FIXED_AMOUNT: float = float(os.getenv('FIXED_AMOUNT', '1000'))

from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.engine import URL
from setting import settings

# Database connection url
conn_URL = URL.create(
    drivername=settings.db_driver,
    username=settings.db_username,
    password=settings.db_password,
    host=settings.db_host,
    port=settings.db_port,
    database=settings.db_database
)

# Database engine for application
engine = create_async_engine(conn_URL)

from contextlib import contextmanager

from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker, Session

from core.config import database_config


class DatabaseHelper:
    def __init__(
            self,
            url: str,
            echo: bool = False,
            echo_pool: bool = False,
            pool_size: int = database_config.pool_size,
            max_overflow: int = database_config.max_overflow,
    ):
        self.engine: Engine = create_engine(
            url=url,
            echo=echo,
            echo_pool=echo_pool,
            pool_size=pool_size,
            max_overflow=max_overflow,
        )

        self.session_factory = sessionmaker(
            bind=self.engine,
            autocommit=False,
            autoflush=False,
        )

    @contextmanager
    def get_db(self):
        db = self.session_factory()
        try:
            yield db
        finally:
            db.close()


db_helper = DatabaseHelper(
    url=str(database_config.url),
    echo=database_config.echo,
    echo_pool=database_config.echo_pool,
    pool_size=database_config.pool_size,
    max_overflow=database_config.max_overflow,
)

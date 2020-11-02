from contextlib import contextmanager

from alembic import command
from singleton_decorator import singleton
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from pokedex.database.migrations import alembic_cfg
from pokedex.settings import DATABASE_URL


@singleton
class DBConnector:
    def __init__(self):
        print("Session criada")
        command.upgrade(alembic_cfg, "head")
        self.engine = create_engine(DATABASE_URL, echo=True)
        self.session = scoped_session(sessionmaker(bind=self.engine))

    @contextmanager
    def conn_session(self):
        session = self.session()
        try:
            yield session
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

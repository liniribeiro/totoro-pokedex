from contextlib import contextmanager

from singleton_decorator import singleton
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

import pokedex
from pokedex.settings import DATABASE_URL


@singleton
class DBConnector:
    def __init__(self):
        print("Session criada")
        pokedex.database.migrations.upgrade()
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

from sqlalchemy import Column, String

from database.models import BaseModel


class Coach(BaseModel):
    __tablename__ = 'coach'

    name = Column(String)
    password = Column(String)

    def __repr__(self):
        return f'Coach {self.name}'

    def to_dict(self):
        return {
            'id': str(self.id),
            'nome': self.name,
            'password': self.password
        }

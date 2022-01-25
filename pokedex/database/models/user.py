from sqlalchemy import Column, String

from pokedex.database.models.base import BaseModel


class UserModel(BaseModel):
    __tablename__ = 'user'

    name = Column(String)
    password = Column(String)
    image = Column(String)

    def __repr__(self):
        return f'Coach {self.name}'

    def to_dict(self):
        return {
            'id': str(self.id),
            'nome': self.name,
            'password': self.password,
            'image': self.image
        }

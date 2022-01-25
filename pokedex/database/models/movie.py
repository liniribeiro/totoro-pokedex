from sqlalchemy import Column, String

from pokedex.database.models.base import BaseModel


class MovieModel(BaseModel):
    __tablename__ = 'movie'

    name = Column(String)
    title = Column(String)
    description = Column(String)
    image = Column(String)
    year = Column(String)

    def __repr__(self):
        return f'Coach {self.name}'

    def to_dict(self):
        return {
            'id': str(self.id),
            'name': self.name,
            'title': self.title,
            'description': self.description,
            'image': self.image,
            'year': self.year
        }

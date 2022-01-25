

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from pokedex.database.models.base import BaseModel


class TestimonyModel(BaseModel):
    __tablename__ = 'testimony'

    message = Column(String)
    user_id = Column(UUID(as_uuid=True), ForeignKey('user.id'), nullable=False)
    movie_id = Column(UUID(as_uuid=True), ForeignKey('movie.id'), nullable=False)

    def __repr__(self):
        return f'Coach {self.name}'

    def to_dict(self):
        return {
            'id': str(self.id),
            'message': self.message,
            'user_id': self.user_id,
            'movie_id': self.movie_id
        }

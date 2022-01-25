from pokedex.database.db_connection import DBConnector
from pokedex.database.models.coach import Coach
from pokedex.database.models.movie import MovieModel
from pokedex.database.models.pokemon import PokemonModel
from pokedex.database.models.user import UserModel


def get_coach_by_username(username):
    with DBConnector().conn_session() as session:
        coach = session.query(Coach).filter_by(name=username).first()
        return coach.to_dict()


def save_coach(coach):
    with DBConnector().conn_session() as session:
        user = Coach(**coach)
        session.add(user)


def save_pokemon(pokemon):
    with DBConnector().conn_session() as session:
        pokemon = PokemonModel(**pokemon)
        session.add(pokemon)


def get_all_pokemons():
    with DBConnector().conn_session() as session:
        pokemons = session.query(PokemonModel).all()
        return [pok.to_dict() for pok in pokemons]


def save_user(user):
    with DBConnector().conn_session() as session:
        user = UserModel(**user)
        session.add(user)


def save_movie(movie):
    with DBConnector().conn_session() as session:
        movie = MovieModel(**movie)
        session.add(movie)

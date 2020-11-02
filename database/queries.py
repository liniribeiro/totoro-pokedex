from database.db_connection import DBConnector
from database.models import Coach
from database.models import PokemonModel


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

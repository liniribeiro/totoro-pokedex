from uuid import uuid4

from flask import Flask, render_template, session
from flask_sqlalchemy import SQLAlchemy

from pokedex.database.migrations import upgrade
from pokedex.database.queries import save_coach, save_pokemon
from pokedex.settings import DATABASE_URL
from pokedex.views.auth import auth_blueprint
from pokedex.views.pokemon import pokemon_blueprint


def make_app() -> Flask:
    flask = Flask(__name__)
    flask.secret_key = 'flask'
    flask.url_map.strict_slashes = False
    flask.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    flask.config['SQLALCHEMY_ECHO'] = True
    flask.config['SQLALCHEMY_BINDS'] = {'default': DATABASE_URL}
    flask.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    flask.register_blueprint(auth_blueprint)
    flask.register_blueprint(pokemon_blueprint)

    db = SQLAlchemy()
    db.init_app(flask)
    upgrade()

    return flask


app = make_app()


def init_database():
    pokemons = [
        {
            'id': str(uuid4()),
            'nome': 'Meowth',
            'especie': 'Arranha Gato',
            'tipo': 'Normal'
        },
        {
            'id': str(uuid4()),
            'nome': 'Charmander',
            'especie': 'Lagarto',
            'tipo': 'Fogo'
        },
        {
            'id': str(uuid4()),
            'nome': 'Clefairy',
            'especie': 'Fada',
            'tipo': 'Fada'
        }
    ]
    coach = {
        'id': str(uuid4()),
        'name': 'alini',
        'password': '123'
    }
    save_coach(coach)
    [save_pokemon(pok) for pok in pokemons]


init_database()


@app.route('/')
def index():
    logged_in = session.get('usuario_logado', None) is not None
    return render_template('home.html', login=logged_in)


if __name__ == "__main__":
    app.run()

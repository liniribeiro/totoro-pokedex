
from flask import Flask, session, render_template
from flask_sqlalchemy import SQLAlchemy

from pokedex.settings import DATABASE_URL, HOST, PORT
from pokedex.views.auth import auth_blueprint
from pokedex.views.movie import movie_blueprint

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
    flask.register_blueprint(movie_blueprint)

    db = SQLAlchemy()
    db.init_app(flask)

    return flask


app = make_app()


@app.route('/')
def index():
    logged_in = session.get('usuario_logado', None) is not None
    return render_template('home.html', login=logged_in)


if __name__ == "__main__":
    app.run(host=HOST, port=PORT)

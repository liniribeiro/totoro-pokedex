from uuid import uuid4

from flask import Blueprint, render_template, session, url_for, request
from werkzeug.utils import redirect

from pokedex.database.queries import get_all_pokemons, save_pokemon

pokemon_blueprint = Blueprint('pokemon', __name__, template_folder='templates')


@pokemon_blueprint.route('/novo')
def novo():
    if not session.get('logged_in', False):
        return redirect(url_for('auth.login', next_page=url_for('pokemon.novo')))
    return render_template('novo.html', titulo='Novo Pokemon')


@pokemon_blueprint.route('/criar', methods=['POST'])
def criar():
    pokemon = {
        'id': str(uuid4()),
        'nome': request.form['nome'],
        'especie': request.form['especie'],
        'tipo': request.form['tipo']
    }
    save_pokemon(pokemon)
    return redirect(url_for('pokemon.lista', login=session.get('logged_in', False)))


@pokemon_blueprint.route('/lista')
def lista():
    pokemon_list = get_all_pokemons()
    return render_template('lista.html', titulo='Pokedex', pokemons=pokemon_list, login=session.get('logged_in', False))

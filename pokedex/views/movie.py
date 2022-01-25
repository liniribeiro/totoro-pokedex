import json

from flask import Blueprint, request

from pokedex.database.queries import save_movie

movie_blueprint = Blueprint('movie', __name__, template_folder='/templates', url_prefix='/movie')


@movie_blueprint.route('/save', methods=('POST',))
def movie_save():
    request_movie = json.loads(request.data)
    save_movie(**request_movie)

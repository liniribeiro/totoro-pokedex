from flask import Blueprint, session, render_template

home_blueprint = Blueprint('', __name__, template_folder='templates')


@home_blueprint.route('/')
def index():
    logged_in = session.get('usuario_logado', None) is not None
    return render_template('home.html', login=logged_in)
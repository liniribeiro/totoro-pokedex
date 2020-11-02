from flask import Blueprint, render_template, request, session, flash, url_for
from werkzeug.utils import redirect

from database.queries import get_coach_by_username

auth_blueprint = Blueprint('auth', __name__, template_folder='/templates')


@auth_blueprint.route('/login')
def login():
    next_page = request.args.get('next_page')
    return render_template('login.html', next_page=next_page)


@auth_blueprint.route('/go', methods=('POST',))
def go():
    trainee_name = request.form['treinadora']
    coach = get_coach_by_username(trainee_name)
    if coach and coach['password'] == request.form['senha']:
        session['usuario_logado'] = coach['id']
        session['logged_in'] = True
        proxima_pagina = request.form['next_page']
        return redirect(proxima_pagina)

    flash(message='Acesso negado, tente novamente!')
    return redirect(url_for('auth.login'))


@auth_blueprint.route('/logout')
def logout():
    session['usuario_logado'] = None
    session['logged_in'] = False
    flash('Treinadora, logue novamente para cadastrar os pokemons que encontrar!')
    return redirect(url_for('index'))



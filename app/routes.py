from app import flask_engine
from flask import render_template

@flask_engine.route('/')
@flask_engine.route('/index')
def abc():
    user = {'username': 'Miguel'}
    return render_template('index.html', title='Home', user=user)

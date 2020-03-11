from app import flask_engine
from flask import render_template

@flask_engine.route('/')
@flask_engine.route('/index')
def abc():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Some nice day here!'
        },
        {
            'author': {'username': 'Max'},
            'body': 'I want to also say something.'
        },
        {
            'author': {'username': 'TomTom'},
            'body': 'I am not a navigator!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

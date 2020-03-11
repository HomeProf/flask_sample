from app import flask_engine
from flask import render_template, flash, redirect
from app.forms import LoginForm


@flask_engine.route('/config')
def config_test():
    x = flask_engine.config['SECRET_KEY']

    return render_template('config.html', x=x)

@flask_engine.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
        form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)

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

from app import flask_engine, db
from flask import render_template, flash, redirect, url_for, request
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from werkzeug.urls import url_parse


@flask_engine.route('/config')
def config_test():
    x = flask_engine.config['SECRET_KEY']

    return render_template('config.html', x=x)

@flask_engine.route('/')
@flask_engine.route('/index')
@login_required
def index():
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
    return render_template('index.html', title='Home', posts=posts)


@flask_engine.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@flask_engine.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@flask_engine.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulation, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

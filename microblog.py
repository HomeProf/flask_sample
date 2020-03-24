from app import flask_engine, db
from app.models import User, Post

@flask_engine.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}

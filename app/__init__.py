from flask import Flask, render_template
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import logging, os
from logging.handlers import SMTPHandler, RotatingFileHandler

flask_engine = Flask(__name__)
flask_engine.config.from_object(Config)
db = SQLAlchemy(flask_engine)
migrate = Migrate(flask_engine, db)
login = LoginManager(flask_engine)
login.login_view = 'login'

from app import routes, models, errors

if not flask_engine.debug:
    if flask_engine.config['MAIL_SERVER']:
        auth = None
        if flask_engine.config['MAIL_USERNAME'] or flask_engine.config['MAIL_PASSWORD']:
            auth = (flask_engine.config['MAIL_USERNAME'],
                    flask_engine.config['MAIL_PASSWORD'])
        secure = None
        if flask_engine.config['MAIL_USE_TLS']:
            secure = ()
        mail_handler = SMTPHandler(
            mailhost=(flask_engine.config['MAIL_SERVER'],
                      flask_engine.config['MAIL_PORT']),
            fromaddr='no-reply@' + flask_engine.config['MAIL_SERVER'],
            toaddrs=flask_engine.config['ADMINS'], subject='Microblog Failure',
            credentials=auth, secure=secure)
        mail_handler.setLevel(logging.ERROR)
        flask_engine.logger.addHandler(mail_handler)

        if not os.path.exists('logs'):
            os.mkdir('logs')
        file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240,
                                           backupCount=10)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(logging.INFO)
        flask_engine.logger.addHandler(file_handler)

        flask_engine.logger.setLevel(logging.INFO)
        flask_engine.logger.info('Microblog startup')

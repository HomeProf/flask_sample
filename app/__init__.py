from flask import Flask, render_template
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

flask_engine = Flask(__name__)
flask_engine.config.from_object(Config)
db = SQLAlchemy(flask_engine)
migrate = Migrate(flask_engine, db)

from app import routes, models

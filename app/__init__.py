from flask import Flask, render_template
from config import Config

flask_engine = Flask(__name__)
flask_engine.config.from_object(Config)

from app import routes

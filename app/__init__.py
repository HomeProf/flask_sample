from flask import Flask, render_template

flask_engine = Flask(__name__)

from app import routes

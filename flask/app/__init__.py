from flask import Flask
from .config import Config
from .init_sql import init_database

def create_app():
    """Create an instance of the class. Flask need __name__"""
    app = Flask(__name__)

    """Setting of app, password or key"""
    #app.config["SECRET_KEY"] = '1234'
    app.config.from_object(Config)
    """Initialize database mysql"""
    init_database()
    return app

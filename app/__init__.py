from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
#create flask extension instance
db = SQLAlchemy()
bootstrap = Bootstrap()
#define app 
def create_app(config_name):
    app = Flask(__name__)
    # Creating the app configurations
    app.config.from_object(config_options[config_name])
    
    #initialising flask extensions
    db.init_app(app)
    bootstrap.init_app(app)
    #registering main blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
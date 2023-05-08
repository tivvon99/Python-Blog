from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from src.common.database import Database
from src.models.blog import Blog
from src.models.post import Post
from src.models.user import User
from datetime import timedelta

def create_app():
    """ Creates the instance of the Flask Object.
    
    Acts as the central configuration object for the entire application. 
    It is used to set up pieces of the application required for extended
    functionality. Eg: Database connection and help with authentication.
    
    A common pattern is creating the application object when the blueprint
    is imported, but if you moe the creating of this object into a
    function, you can created mulitple instances of this app later. Better
    for testing and multiple instances.
    
    __name__ tells us how to import from files relative to this one.
    
    Database is initialized by a special method, before_first_request.
    
    .register_blueprint extends the flask page with its contents.
    """
    
    app = Flask(__name__)                   # instance of the Flask object
    app.secret_key="California"
    app.permanent_session_lifetime = timedelta(minutes=5)
    
    @app.before_first_request
    def initialize_database():
        Database.initialize()
    
    # blueprint for auth routes in app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
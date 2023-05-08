'''
Acts as the central configuration object for the entire application. 
It is used to set up pieces of the application required for extended
functionality. Eg: Database connection and help with authentication.

__name__ tells us how to import from files relative to this one.

'''

from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from src.common.database import Database
from src.models.blog import Blog
from src.models.post import Post
from src.models.user import User
from datetime import timedelta

def create_app():
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


"""
    app = Flask(__name__, static_url_path='/static')  # '__main__'
    app.secret_key = "California"

    if __name__ == '__main__':
        app.run(port=4995, debug=True)
"""
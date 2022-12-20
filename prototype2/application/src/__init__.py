from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from src.common.database import Database
from src.models.blog import Blog
from src.models.post import Post
from src.models.user import User
from datetime import timedelta

"""
app = Flask(__name__, static_url_path='/static')  # '__main__'
app.secret_key = "California"
"""

def create_app():
    app = Flask(__name__)
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
    if __name__ == '__main__':
        app.run(port=4995, debug=True)
"""
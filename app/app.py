"""The app module, containing the app factory function."""
from flask import Flask

from app.extensions import db, migrate, login_manager


def create_app(config_object="app.config"):
    # Create application factory. Param config_object, the configuration object to use.
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)

    return app



def register_extensions(app):
    # Initialize the extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    return None

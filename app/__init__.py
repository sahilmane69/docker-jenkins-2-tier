from flask import Flask
from config.settings import config


def create_app(env="development"):
    """
    App factory pattern — lets us create different app instances
    for testing, development, and production. This is the DevOps-friendly way.
    """
    app = Flask(__name__)

    # Load config based on environment (set via ENV variable in Docker/CI)
    app.config.from_object(config[env])

    # Register route blueprints
    from app.routes.main import main_bp
    from app.routes.health import health_bp
    from app.routes.api import api_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(health_bp)
    app.register_blueprint(api_bp, url_prefix="/api")

    return app
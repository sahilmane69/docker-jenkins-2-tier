import os


class BaseConfig:
    """Shared settings across all environments."""
    SECRET_KEY = os.environ.get("SECRET_KEY", "change-me-in-production")
    DEBUG = False
    TESTING = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class TestingConfig(BaseConfig):
    """
    TESTING = True disables error propagation so your test client
    gets real HTTP error responses instead of exceptions.
    """
    TESTING = True
    DEBUG = True


class ProductionConfig(BaseConfig):
    """
    In production, everything comes from environment variables —
    never hardcode secrets. Your CI/CD pipeline injects these.
    """
    SECRET_KEY = os.environ.get("SECRET_KEY")  # must be set in prod!
    DEBUG = False


# Map string names to classes — used by create_app()
config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
}
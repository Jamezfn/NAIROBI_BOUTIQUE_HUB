import os
class Config:
    """
    Configuration class for setting up Flask application settings.
    """
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///site.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'kista_amezutd')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'kista_amezutd')

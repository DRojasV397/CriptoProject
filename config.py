import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your_secret_key')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'mysql+pymysql://flask_user:your_password@localhost/flask_app')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

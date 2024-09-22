import os
from datetime import timedelta

class Config(object):
    APPNAME = 'app'
    ROOT = os.path.abspath(APPNAME)
    UPLOAD_PATH = '/static/upload/'
    SERVER_PATH = ROOT + UPLOAD_PATH

    USER = os.environ.get('POSTGRES_USER', 'pawtouka')
    PASSWORD = os.environ.get('POSTGRES_PASSWORD', 'sofal1tl')
    HOST = os.environ.get('POSTGRES_HOST', '127.0.0.1')
    PORT = os.environ.get('POSTGRES_PORT', 5532)
    DB = os.environ.get('POSTGRES_DB', 'mydb')

    SQLALCHEMY_DATABASE_URI = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"
    SECRET_KEY = 'CNDIMCHIHGCBY4BF4I2NCBDSI'
    SQLALCHEMY_TARCK_MODOFICATIONS = True
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=10)

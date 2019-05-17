import os

# postgres_local_base = os.environ['DB_URL]

# set basedir
basedir = os.path.abspath(os.path.dirname(__file__))

class config:
    SECRET_KEY = os.getenv('SECRET_KEY', '*M4ManG!g0r3ngaN|\/|/-|nt4p#J1\/\/A*#z')
    DEBUG = False

class DevelopmentConfig(config):
    #SQLALCHEMY_DATABASE_URI = postgres_local_base
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'proto.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestingConfig(config):
    DEBUG =True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'proto.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(config):
    DEBUG = False
    # SQLALCHEMY_DATABASE_URI = postgres_local_base


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = config.SECRET_KEY
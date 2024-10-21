import os

from dotenv import load_dotenv
load_dotenv()


class Config:
    """
    Configuration de base qui s'applique à tous les environnements.
    """
    PROJECT = "big-data"
    FLASK_ENV = os.getenv('FLASK_ENV', 'production')
    APP_VERSION = "0.0.0"

    DEBUG = False
    TESTING = False
    LOG_FOLDER = os.path.join('tmp' 'logs')

    CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.
    CSRF_ENABLED = True,
    CORS_ORIGIN_WHITELIST = [
        'http://0.0.0.0'
    ]

    def __setitem__(self, key, item):
        self.__dict__[key] = item

    def __getitem__(self, key):
        return self.__dict__[key]



class DevelopmentConfig(Config):
    """
    Configuration spécifique à l'environnement de développement.
    """
    FLASK_ENV="development"
    DEBUG = True


class ReleaseConfig(Config):
    """
    Configuration spécifique pour les tests unitaires.
    """
    FLASK_ENV="release"
    TESTING = True
    


class TestConfig(Config):
    """
    Configuration spécifique pour les tests unitaires.
    """
    TESTING = True



class ProductionConfig(Config):
    """
    Configuration spécifique à l'environnement de production.
    """
    FLASK_ENV="production"
    DEBUG = False





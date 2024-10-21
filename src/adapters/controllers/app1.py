import os
import sys
import logging
from flask_cors import CORS
from dotenv import load_dotenv
from flask import Flask, render_template, jsonify, request

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from config import Config

from adapters.controllers.apis.file.get_file import api_file_blueprint
from adapters.controllers.apis.version.get_version import api_version_blueprint

from adapters.controllers.pages.routes import page_routes_blueprint


def create_app(config=None, root_path=None, static_folder=None, template_folder=None):
    """Create a Flask app."""



    app = Flask(__name__, 
                instance_relative_config=True, root_path=root_path,
                static_folder=static_folder,
                template_folder=template_folder)

    CORS(app, resources={r"/api/*": {"origins": "*"}})
    configure_app(app, config)
    register_blueprints(app)
    configure_hook(app)
    error_handlers(app)


    return app


def configure_app(app, config=None):
    FLASK_ENV = os.getenv('FLASK_ENV', 'development')
    if config:
        app.config.from_object(config)

    env_config_class = f'config.{FLASK_ENV.capitalize()}Config'
    app.config.from_object(env_config_class)
    app.config.from_pyfile('config.py', silent=True)

    print(f"Environment: {app.config['FLASK_ENV']}")
    print(f"Debug mode: {app.config['DEBUG']}")
    print(f"Testing mode: {app.config['TESTING']}")


def register_blueprints(app):
    """
    Enregistrement des Blueprints pour séparer les routes API et les vues HTML.
    """
    # API Blueprint (point d'entrée pour les requêtes JSON)
    app.register_blueprint(api_version_blueprint, url_prefix='/api')
    app.register_blueprint(api_file_blueprint, url_prefix='/api')

    # Home Blueprint (point d'entrée pour les pages rendues HTML)
    app.register_blueprint(page_routes_blueprint, url_prefix='/')


def error_handlers(app):
    @app.errorhandler(404)
    def page_not_found(error):
        pathname = request.path
        flask_env = app.config['FLASK_ENV']

        if pathname.startswith('/api'):
            if flask_env == 'production':
                return jsonify({'message': 'Not Found'}), 404
            else:
                return jsonify({'message': 'Not Found', 'error': str(error)}), 404
        else:
            if flask_env == 'production':
                return render_template("errors/404.html"), 404
            else:
                return render_template("errors/404.html", error=error), 404
            
            
    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({'error': 'Erreur interne du serveur'}), 500
    

def configure_hook(app):

    @app.before_request
    def before_request():
        pass



root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
static_folder = os.path.join(root_path, 'adapters', 'static')
template_folder = os.path.join(root_path, 'adapters', 'templates')

logger = logging.getLogger(__name__)
app = create_app(Config,
                 root_path=root_path,
                 static_folder=static_folder,
                 template_folder=template_folder)

if __name__ == '__main__':
    # Lancer l'application avec le bon environnement (développement par défaut)
    app.run(host='0.0.0.0', port=5000)

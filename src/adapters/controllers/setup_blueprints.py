from adapters.controllers.apis.file.get_file import api_file_blueprint
from adapters.controllers.apis.version.get_version import api_version_blueprint

from adapters.controllers.pages.routes import page_routes_blueprint

def setup_blueprints(app):
    
    # API Blueprint (point d'entrée pour les requêtes JSON)
    app.register_blueprint(api_version_blueprint, url_prefix='/api')
    app.register_blueprint(api_file_blueprint, url_prefix='/api')

    # Home Blueprint (point d'entrée pour les pages rendues HTML)
    app.register_blueprint(page_routes_blueprint, url_prefix='/')

    return app
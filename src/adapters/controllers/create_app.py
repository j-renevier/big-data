import os
from pathlib import Path
from flask import Flask

from adapters.controllers.cors import setup_cors
from adapters.controllers.configure_app import configure_app
from adapters.controllers.management import setup_management
from adapters.controllers.setup_blueprints import setup_blueprints
from adapters.controllers.setup_error_handler import setup_error_handler

def create_app(config=None):
    
    root_path = Path(__file__).resolve().parent.parent
    static_folder = os.path.join(root_path, 'adapters', 'static')
    template_folder = os.path.join(root_path, 'adapters', 'templates')

    app = Flask(__name__, 
                instance_relative_config=True, root_path=root_path,
                static_folder=static_folder,
                template_folder=template_folder)
    
    app = configure_app(app, config)
    app = setup_cors(app)
    app = setup_blueprints(app)
    app = setup_error_handler(app)
    app = setup_management(app)


    return app
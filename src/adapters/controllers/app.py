import os
import sys
import logging

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from config import Config
from adapters.controllers.create_app import create_app

logger = logging.getLogger(__name__)

if __name__ == '__main__':

    app = create_app(Config)
    # Lancer l'application avec le bon environnement (développement par défaut)
    app.run(host='0.0.0.0', port=5000)

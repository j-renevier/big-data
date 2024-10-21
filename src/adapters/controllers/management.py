import logging

logger = logging.getLogger(__name__)

def setup_management(app):

    @app.cli.command("print_config")
    def print_config():
        print(app.config)

    return app
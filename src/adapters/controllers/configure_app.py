import os
import sys
import logging
from flask_cors import CORS
from dotenv import load_dotenv
from flask import Flask, render_template, jsonify, request

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))


def configure_app(app, config=None):
    FLASK_ENV = 'development'
    if config:
        app.config.from_object(config)

    env_config_class = f'config.{FLASK_ENV.capitalize()}Config'
    app.config.from_object(env_config_class)
    app.config.from_pyfile('config.py', silent=True)

    print(f"Environment: {app.config['FLASK_ENV']}")
    print(f"Debug mode: {app.config['DEBUG']}")
    print(f"Testing mode: {app.config['TESTING']}")

    return app
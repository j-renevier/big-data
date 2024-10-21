from flask import Blueprint, jsonify

api_file_blueprint = Blueprint('api_file', __name__)

@api_file_blueprint.route('/file', methods=['GET'])
def get_all_files():
    """
    Retourner toutes les données des fichiers.
    """

    return 'get file', 200

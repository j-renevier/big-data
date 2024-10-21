from flask import Blueprint, render_template, redirect


page_routes_blueprint = Blueprint('home', __name__)

@page_routes_blueprint.route('/home', methods=['GET'])
def home_page():
    """
    Rendre la page d'accueil de l'application.
    """
    return render_template('home/index.html')

@page_routes_blueprint.route('/', methods=['GET'])
def root_page():
    """
    Redirection vers la page d'accueil.
    """
    return redirect('/home', code=302)

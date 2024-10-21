from flask import render_template, jsonify, request

def setup_error_handler(app):
    @app.errorhandler(404)
    def page_not_found(error):
        pathname = request.path
        flask_env = app.config['FLASK_ENV']

        if pathname.startswith('/api'):
            if flask_env == 'production':
                return jsonify({'message': str(error), 'content': '', 'error': str(error)}), 404
            else:
                return jsonify({'message': str(error), 'content': '', 'error': str(error)}), 404
        else:
            if flask_env == 'production':
                return render_template("errors/404.html"), 404
            else:
                return render_template("errors/404.html", error=error), 404
            
            
    @app.errorhandler(500)
    def internal_server_error(error):
        pathname = request.path
        flask_env = app.config['FLASK_ENV']

        if pathname.startswith('/api'):
            if flask_env == 'production':
                return jsonify({'message': str(error), 'content': '', 'error': str(error)}), 500
            else:
                return jsonify({'message': str(error), 'content': '', 'error': str(error)}), 500
        else:
            if flask_env == 'production':
                return jsonify({'message': str(error), 'content': '', 'error': str(error)}), 500
            else:
                return jsonify({'message': str(error), 'content': '', 'error': str(error)}), 500
            
    return app
    
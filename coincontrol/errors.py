from flask import jsonify, render_template, request
from flask_wtf.csrf import CSRFError

from coincontrol.user import main_bp


@main_bp.app_errorhandler(404)
def page_not_found(e):
    if request.accept_mimetypes.accept_json and \
        not request.accept_mimetypes.accept_html:
        response = jsonify({'error': 'Not Found'})
        response.status_code = 404
    return render_template('404.html'), 404

@main_bp.app_errorhandler(500)
def internal_server_error(e):
    if request.accept_mimetypes.accept_json and \
        not request.accept_mimetypes.accept_html:
        response = jsonify({'error': 'Internal Server Error'})
        response.status_code = 404
    return render_template('500.html'), 500


def forbidden(message):
    response = jsonify({'error': 'forbidden', 'message': message})
    response.status_code = 403
    return response



@main_bp.errorhandler(CSRFError)
def handle_csrf_error(e):
    return render_template('csrf_error.html', reason=e.description), 400
from app.errors import bp
from flask import render_template
from app import db


@bp.app_errorhandler(404)
def not_found(error):
    return render_template('errors/404.html'), 404

@bp.app_errorhandler(500)
def internal_server_error(error):
    '''
    Function that handles server error
    '''
    db.sessions.rollback()
    return render_template('errors/500.html'), 500 
from app.errors import bp
from flask import render_template


@bp.app_errorhandler(404)
def not_found(error):
    return render_template('errors/404.html'), 404
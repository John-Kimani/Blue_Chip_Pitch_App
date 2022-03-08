from flask import redirect, render_template, url_for
from app.main import bp
# from flask_login import current_user, login_user, logout_user, login_required


@bp.route('/')
@bp.route('/index')
# @login_required
def index():
    '''
    View function that set display on home page
    '''
    # if current_user.is_authenticated:
    #     return redirect(url_for('index'))

    title = "HOME"
    return render_template('index.html', title=title)
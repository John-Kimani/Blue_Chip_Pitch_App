from flask import render_template, redirect,url_for,flash
from app.main import bp
from flask_login import current_user, login_required
from app import db
from app.main.forms import PitchForm
from app.models import Pitch


@bp.route('/', methods=['GET', 'POST'] )
@bp.route('/index', methods=['GET', 'POST'] )
@login_required
def index():
    '''
    View function that set display on home page
    '''
    # if current_user.is_authenticated:
    #     return redirect(url_for('main.index'))
    title = "HOME"
    form = PitchForm()
    if form.validate_on_submit():
        pitch = Pitch(body=form.body.data, author=current_user)
        db.session.add(pitch)
        db.session.commit()
        flash('Your pitch has been uploaded')
        return redirect(url_for('main.index'))
    all_pitches = Pitch.query.order_by(Pitch.timestamp.desc()).all()

    return render_template('index.html', title=title, form=form, all_pitches=all_pitches)
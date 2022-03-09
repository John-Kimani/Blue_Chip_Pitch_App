from flask import redirect, render_template, url_for
from app.main import bp
from flask_login import login_required
from app import db
from app.main.forms import PitchForm
from app.models import Pitch


@bp.route('/')
@bp.route('/index')
@login_required
def index():
    '''
    View function that set display on home page
    '''
    title = "HOME"
    pitch= Pitch()
    db.session.add(pitch)
    db.session.commit()
    print('*'*30)
    print(pitch)

    all_pitch = Pitch.query.all()
    print('*'*30)
    print(all_pitch)

    form = PitchForm()
    return render_template('index.html', title=title, allpitch=all_pitch, form=form)
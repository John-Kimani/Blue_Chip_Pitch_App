from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
from app.models import Pitch

class PitchForm(FlaskForm):
    '''
    Class that handles pitch creation buy users
    '''
    body = StringField('Enter your pitch', validators=[DataRequired()])
    submit = SubmitField('Submit Pitch')
    
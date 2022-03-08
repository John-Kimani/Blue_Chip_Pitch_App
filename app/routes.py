from flask import render_template
from app import app

# from flask_login import login_required



@app.route('/')
@app.route('/index')
# @login_required
def index():
    '''
    View function that set display on home page
    '''
    title = "HOME"
    return render_template('index.html', title=title)



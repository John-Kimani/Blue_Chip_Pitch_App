from flask import render_template
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    '''
    View function that set display on home page
    '''
    title = "HOME"
    return render_template('index.html', title=title)

@app.route('/login')
def login():
    '''
    View function that set display on login page
    '''
    form = LoginForm()
    title = "LogIn"
    return render_template('login.html', title=title, form=form )
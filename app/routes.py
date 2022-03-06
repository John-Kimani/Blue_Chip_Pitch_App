from flask import render_template, flash, redirect, url_for
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

@app.route('/login', methods=['GET','POST'])
def login():
    '''
    View function that set display on login page
    '''
    form = LoginForm()
    title = "LogIn"
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title=title, form=form )
from flask import render_template, flash, redirect, url_for
from app import app,db
from app.forms import LoginForm, SignupForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User


@app.route('/')
@app.route('/index')
@login_required
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
    current user from flask login is a preventive measure for a user in session to double log in
    '''
    if current_user.is_authenticated:
        '''
        Redirects logged in user to home page
        '''
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        '''
        Creates user variable after successful login
        Methods:
            first assigns the unique username to be true
        '''
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            '''
            Condition to handle invalid user input
            Returns:
                Invalid response retains user on login page to enable them try again
                Valid reponse redirects user to the authorized home page
            '''
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        flash('You are logged in succesfully')
        return redirect(url_for('index'))
    title = "LogIn"
    return render_template('login.html', title=title, form=form )

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    '''
    Function that handles registration page
    '''
    if current_user.is_authenticated:
        '''
        Logic that handles user approval
        '''
        return redirect(url_for('index'))
    form = SignupForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password_hash=form.password.data)
        '''
        Condition that creates a new user variable and add user to database
        Returns:
            Successful new users to login
        '''
        db.session.add(user)
        db.session.commit()
        flash('Congratulatons you are now a registered user')
        return redirect('login')
    return render_template('signup.html', title="Register", form=form)


@app.route('/logout')
def logout():
    '''
    Function that handles logout
    Returns:
        Log out user to login page
    '''
    logout_user()
    return redirect(url_for('login'))
from app import app
from flask import render_template, flash, redirect,  url_for
from flask_login import current_user, login_user
from app.forms import LoginForm

@app.route('/index')
def index():
    user = {'username': 'Mario', 'age': '26 years old'}
    return render_template("index.html", user=user)

@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = form.username.data
        passwd = form.password.data
        if user == "Mario" and passwd == "patata55":
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password')
            return redirect(url_for('login'))
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)
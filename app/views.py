from app import application as pages
from flask import render_template, request, redirect, url_for, flash, make_response, session
from flask_login import login_required, login_user,current_user, logout_user
from programm.msg import create_user
from .model import User
from app import db
from .forms import LoginForm
import plotly.express as px
from programm.graphs import create_graph
@pages.route('/home/')
@login_required
def home():
    return render_template('home.html')
@pages.route('/analys/')
@login_required
def analys():
    data = {
    'x': [1, 2, 3, 4, 5],
    'y': [10, 11, 12, 13, 14]}
    data2 = {
    'x': [4, 2, 3, 4, 5],
    'y': [10, 15, 11, 13, 14]}
    first_g = create_graph(data)
    return render_template('analysys.html', plot = first_g, plot2 =create_graph(data2))
@pages.route('/', methods=['post', 'get'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.query(User).filter(User.username == form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        flash("Invalid username/password", 'error')
        return redirect(url_for('login'))
    return render_template('login.html', form=form)

@pages.route('/logout/')
@login_required
def logout():
    logout_user()
    flash("You have been logged out.")
    return redirect(url_for('login'))
@pages.route('/cookie/')
def cookie():
    if not request.cookies.get('foo'):
        res = make_response("Setting a cookie")
        res.set_cookie('foo', 'bar', max_age=60*60*24*7)
    else:
        res = make_response("Value of cookie foo is {}".format(request.cookies.get('foo')))
    return res


@pages.route('/delete-cookie/')
def delete_cookie():
    res = make_response("Cookie Removed")
    res.set_cookie('foo', 'bar', max_age=0)
    return res


@pages.route('/about')
@login_required
def about():
    return render_template('about.html')
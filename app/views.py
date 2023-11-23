from app import application as pages
from flask import render_template, request, redirect, url_for, flash, make_response, session
import plotly.express as px
from programm.graphs import create_graph

@pages.route('/')
def home():
    return render_template('home.html')

@pages.route('/analys')
def analys():
    data = {
    'x': [1, 2, 3, 4, 5],
    'y': [10, 11, 12, 13, 14]}
    data2 = {
    'x': [4, 2, 3, 4, 5],
    'y': [10, 15, 11, 13, 14]}
    first_g = create_graph(data)
    return render_template('analys.html', plot = first_g, plot2 =create_graph(data2))

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
def about():
    return render_template('about.html')
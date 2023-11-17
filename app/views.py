from app import application as pages
from flask import render_template
from programm.msg import message
@pages.route('/')
def home():
    Message = message.write_message('Hello world')
    return render_template('main.html', message =  Message)

@pages.route('/about')
def about():
    return render_template('about.html')
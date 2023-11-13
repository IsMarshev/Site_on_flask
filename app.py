from flask import Flask, render_template
from programm.msg import message
app = Flask(__name__)

@app.route('/')
def home():
    Message = message.write_message('Hello world')
    return render_template('main.html', message =  Message)

@app.route('/about')
def about():
    return render_template('about.html')
#for run use command: python app.py
if __name__=='__main__':
    app.run(debug=True)
from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    "Show the welcome page"
    return "welcome"

@app.route('/welcome/home')
def welcome_home():
    "Welcome users to the home screen"
    return "welcome home"

@app.route('/welcome/back')
def welcome_back():
    "Welcome a returning user"
    return "welcome back"
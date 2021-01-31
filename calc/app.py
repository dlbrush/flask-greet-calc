from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def show_add():
    "Show the sum of the arguments in the query string"
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(add(a, b))

@app.route('/sub')
def show_sub():
    "Show the difference of the arguments in the query string"
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(sub(a, b))

@app.route('/mult')
def show_mult():
    "Show the product of the arguments in the query string"
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(mult(a, b))

@app.route('/div')
def show_div():
    "Show the product of the arguments in the query string"
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(div(a, b))

@app.route('/math/<operation>')
def show_math(operation):
    "Show the result of the operation specified in the URL"
    a = int(request.args['a'])
    b = int(request.args['b'])
    result = eval(f"{operation}({a}, {b})")
    return str(result)
# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div 

app = Flask(__name__)

# @app.route('/add')
# def do_add():
#     a = int(request.args.get('a'))
#     b = int(request.args.get('b'))
#     sum = add(a, b)
#     return str(sum)

# @app.route('/sub')
# def do_sub():
#     a = int(request.args.get('a'))
#     b = int(request.args.get('b'))
#     difference = a- b
#     return str(difference)

# @app.route('/mult')
# def mult():
#     a = int(request.args.get('a'))
#     b = int(request.args.get('b'))
#     product = a * b
#     return str(product)

# @app.route('/div')
# def div():
#     a = int(request.args.get('a'))
#     b = int(request.args.get('b'))
#     quotient = a / b
#     return str(quotient)

operators = {
    'add': add,
    'sub': sub,
    'div': div,
    'mult': mult
}

@app.route('/math/<oper>')
def do_math(oper):
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = operators[oper](a, b)
    return str(result)


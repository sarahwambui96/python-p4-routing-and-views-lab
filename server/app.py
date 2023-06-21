#!/usr/bin/env python3

from flask import Flask, make_response

app = Flask(__name__)

@app.route("/")
def index():
    response_body = "<h1>Python Operations with Flask Routing and Views</h1>"
    response = make_response(response_body, 200)
    return response
@app.route("/print/<string:parameter>")
def print_string(parameter):
    print(parameter)
    response_body = parameter
    response = make_response(response_body, 200)
    return response
@app.route("/count/<int:parameter>")
def count(parameter):
    response_body = '\n'.join(str(i) for i in range(parameter))
    response = make_response(response_body, 200)
    return response
@app.route("/math/<int:num1>/<operation>/<int:num2>")
def math(num1, operation, num2):
    result = None

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

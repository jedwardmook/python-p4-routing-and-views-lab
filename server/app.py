#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
  print(parameter)
  return f'{parameter}'

@app.route('/count/<int:parameter>')
def count(parameter):
  def count_to_parameter():
    for n in range(parameter):
      yield f'{n}\n'
  return count_to_parameter()

@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, operation, num2):
  result = 0
  if operation == "+":
    result = (int(num1) + int(num2))
  elif operation == "-":
    result = (int(num1) - int(num2))
  elif operation == "*":
    result = (int(num1) * int(num2))
  elif operation == "div":
    result = (int(num1) / int(num2))
  return str(result)

if __name__ == '__main__':
  app.run(port=5555, debug=True)

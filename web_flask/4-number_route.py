#!/usr/bin/python3
"""
script that creates a Flask web application with the specified routes
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    '''display hello HBNB'''
    return 'Hello HBNB'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''Displays HBNB'''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_c(text='is_cool'):
    '''Display C followed by variable'''
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python/<text>', strict_slashes=False)
def display_python(text):
    '''display "Python " followed by the value of the text variable'''
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    '''display n'''
    return '{} is a number'.format(n)


if __name__ == '__main__':
    '''Run the Flask app on 0.0.0.0, port 5000'''
    app.run(host='0.0.0.0', port=5000)

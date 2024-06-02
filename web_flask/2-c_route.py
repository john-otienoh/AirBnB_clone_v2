#!/usr/bin/python3
"""
script using Flask to create a web application with three routes as specified
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    '''Displays hello HBNB'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''Displays HBNH'''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_text(text):
    '''Displays C followed by text'''
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


if __name__ == '__main__':
    ''' Run the Flask app on 0.0.0.0, port 5000'''
    app.run(host='0.0.0.0', port=5000)

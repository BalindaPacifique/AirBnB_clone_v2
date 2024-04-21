#!/usr/bin/python3
""" defines a Flask web application with two routes"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Defines a route for the root URL ("/") """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """ Defines a route for "/hbnb" """
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

#!/usr/bin/python3
""" defines a simple Flask web application"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Defines a route for the root URL ("/") that displays "Hello HBNB!" """
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


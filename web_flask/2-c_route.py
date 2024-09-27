#!/usr/bin/python3
"""Start a Flask web Application listening on 0.0.0.0 port 5000"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """Replace underscores with spaces"""
    text = text.replace('_', ' ')
    return "C {}".format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
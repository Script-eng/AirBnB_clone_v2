#!/usr/bin/python3
"""Start a Flask web app listening on 0.0.0.0 port 5000"""
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


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    """Replace underscores with spaces"""
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """Display “n is a number” only if n is an integer"""
    if isinstance(n, int):
        return "{} is a number".format(n)
    else:
        return "", 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

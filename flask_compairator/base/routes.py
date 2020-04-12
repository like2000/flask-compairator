from flask import render_template

from . import blueprint


@blueprint.route('/index')
def index():
    return render_template("index.html", var=None)


@blueprint.route('/python_process')
def python_process():
    print("Hello! You're in a python function now!")
    return ("Nothing")

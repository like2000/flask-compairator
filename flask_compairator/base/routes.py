from flask import render_template

from . import blueprint


@blueprint.route('/index')
def index():
    return render_template("index.html", var=None)

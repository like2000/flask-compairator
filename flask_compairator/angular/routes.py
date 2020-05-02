from flask import render_template, url_for

from . import blueprint


@blueprint.route("/run")
def run():
    return render_template('angular.html')

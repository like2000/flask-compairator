import numpy as np
from flask import render_template

from . import blueprint


@blueprint.route('/index')
def index():
    return render_template("index.html", label=None)


@blueprint.route('/python_process', methods=['POST'])
def python_process():
    r = np.random.randint(1, 10, 1)[0]
    print(f"Hello! You're in a python function now! Your new number picked is: {r}.")
    return render_template("index.html", label=str(r))

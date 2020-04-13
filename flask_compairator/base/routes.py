import numpy as np
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

from . import blueprint

tries = 0
r = np.random.randint(1, 6, 1)[0]
animals = dict(cat=1, dog=2, dragon=3, dove=4, spider=5)


@blueprint.route('/index')
def index():
    return render_template("index.html", label=None)


@blueprint.route('/python_process', methods=['GET', 'POST'])
def python_process():
    global tries, r
    if request.method == 'POST':
        if tries > 2:
            tries = 0
            r = np.random.randint(1, 6, 1)[0]
            print(np.random.randint(1, 6, 10))
            return redirect(url_for('home_blueprint.over'))

        for key, name in request.form.items():
            if animals.get(name) == r:
                tries = 0
                r = np.random.randint(1, 6, 1)[0]
                text = f"Yes! You found a {name}!"
                return render_template("index.html", label=text, color="w3-green")
            else:
                tries = tries + 1
                text = f"Sorry, no {name} here... try again!"
                return render_template("index.html", label=text, color="w3-red")

    elif request.method == 'GET':
        return render_template("index.html")

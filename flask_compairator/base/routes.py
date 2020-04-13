import numpy as np
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

from . import blueprint

tries = 0
animals = dict(cat=1, dog=2, dragon=3, dove=4, spider=5)


@blueprint.route('/index')
def index():
    return render_template("index.html", label=None)


@blueprint.route('/python_process', methods=['GET', 'POST'])
def python_process():
    global tries
    if request.method == 'POST':
        rnum = np.random.randint(1, 5, 1)[0]
        for key, name in request.form.items():
            print(key, name, animals.get(name), rnum, tries)

            if animals.get(name) == rnum:
                tries = 0
                text = f"Yes! You found your {name}!"
                return render_template("index.html", label=text, color="w3-green")
            else:
                tries = tries + 1
                if tries > 3:
                    return redirect(url_for('home'))
                else:
                    text = f"No - {name} not found... try again!"
                    return render_template("index.html", label=text, color="w3-red")

    elif request.method == 'GET':
        return render_template("index.html")

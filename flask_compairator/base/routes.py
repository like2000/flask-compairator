import numpy as np
from flask import render_template
from flask import request

from . import blueprint

animals = dict(cat=1, dog=2, dragon=3, dove=4, spider=5)


@blueprint.route('/index')
def index():
    return render_template("index.html", label=None)


@blueprint.route('/python_process', methods=['GET', 'POST'])
def python_process(tries=0):
    if request.method == 'POST':
        rnum = np.random.randint(1, 5, 1)[0]
        name = request.form.get('value')
        print(request.form, request.args, request.form.get('cat'), name)
        # print(f"Hello! You're in a python function now! Your new number picked is: {r}.")

        if animals.get(name) == rnum:
            text = f"Yes! You found your {name}!"
            return render_template("index.html", label=text, type="w3-green")
        else:
            tries += 1
            if tries > 3:
                return render_template("")
            else:
                text = f"No - {name} not found... try again!"
                return render_template("index.html", label=text, type="w3-red")

    elif request.method == 'GET':
        return render_template("index.html")

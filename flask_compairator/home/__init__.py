from flask import Blueprint

name = 'home'

blueprint = Blueprint(
    name + '_blueprint',
    import_name=__name__,
)

from flask import Blueprint

name = 'game_a'

blueprint = Blueprint(
    name + '_blueprint',
    import_name=__name__,
)

from flask import Blueprint

name = 'part_a'

blueprint = Blueprint(
    name + '_blueprint',
    import_name=__name__,
)

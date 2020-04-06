from flask import Blueprint

name = 'module_a'

blueprint = Blueprint(
    name + '_blueprint',
    import_name=__name__,
    static_folder='static',
    template_folder='templates',
)

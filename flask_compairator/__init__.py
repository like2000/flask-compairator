from importlib import import_module

from flask import Flask
from flask import redirect
from flask import url_for


def register_blueprints(server: Flask):
    for module_name in ('base', 'data', 'module_a'):
        module = import_module(f'flask_compairator.{module_name}.routes')
        server.register_blueprint(module.blueprint, url_prefix=f'/{module_name}')


def create_app():
    server = Flask(
        __name__,
        static_folder='base/static'
    )

    register_blueprints(server)

    @server.route("/")
    def home():
        return redirect(url_for('base_blueprint.index'))

    return server

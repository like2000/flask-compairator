from . import blueprint


@blueprint.route("/test")
def test():
    return "<h1>A hidden landing page!</h1>"

from . import blueprint


@blueprint.route("/over")
def over():
    return '''
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">

    <div class="w3-panel w3-black w3-center w3-padding-32"><h1 class="w3-xlarge">Game over!</h1></div>'
    
    <div class="w3-button w3-brown w3-padding-large w3-center" style="margin: auto; display: block; width: 300px">
    <a href="/base/index"> Restart </a>
    </div>
    '''

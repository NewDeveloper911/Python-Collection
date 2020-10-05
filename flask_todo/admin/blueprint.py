from flask import Blueprint, render_template

blueprint = Blueprint("blueprint",  __name__, static_folder="static", template_folder="templates")
'''
Here, I have just told my program of the locations of my static (unchanging files) and template (html webpages) folders
'''

@blueprint.route("/home")
@blueprint.route("/") 
def home():
    '''
    if it is the same route as of a route in hello.py, this one 
    will run instead of hello.py because of the 
    register_blueprint()
    '''
    return render_template("base.html")

@blueprint.route("/test")
def test():
    return f"<h1>Yo</h1>"
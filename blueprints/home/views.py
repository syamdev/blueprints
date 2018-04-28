from flask import render_template, Blueprint

home = Blueprint(
    'home', #name of module
    __name__,
    template_folder='templates' # templates folder
)
@home.route('/')
def index():
    return render_template("index.html")
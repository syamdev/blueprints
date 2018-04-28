from flask import render_template, Blueprint

about = Blueprint(
    'about', #name of module
    __name__,
    template_folder='templates' # templates folder
)
@about.route('/')
def index():
    return render_template("about.html")
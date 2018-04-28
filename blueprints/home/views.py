from flask import render_template, Blueprint

mod1 = Blueprint(
    'mod1', #name of module
    __name__,
    template_folder='templates' # templates folder
)
@mod1.route('/')
def index():
    return render_template("index.html")
from flask import render_template, Blueprint

mod2 = Blueprint(
    'mod2', #name of module
    __name__,
    template_folder='templates' # templates folder
)
@mod2.route('/')
def index():
    return render_template("index.html")
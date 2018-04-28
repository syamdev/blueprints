from flask import Flask
from blueprints.home.views import home
from blueprints.about.views import about

app = Flask(__name__)
app.register_blueprint(home, url_prefix='/home')
app.register_blueprint(about, url_prefix='/about')
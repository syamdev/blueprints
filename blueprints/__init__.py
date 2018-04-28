from flask import Flask
from blueprints.home.views import mod1
from blueprints.about.views import mod2

app = Flask(__name__)
app.register_blueprint(mod1, url_prefix='/home')
app.register_blueprint(mod2, url_prefix='/about')
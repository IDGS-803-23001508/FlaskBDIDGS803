from inicio import inicio
from flask import render_template

@inicio.route("/")
@inicio.route("/index")
def index():
    return render_template("inicio/index.html")
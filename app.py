from init import app
from flask import render_template
from models import *
from api import api

@app.route("/")
def hello_world():
    return render_template('home.html')

@app.route("/another")
def another():
    return render_template('another.html')

app.register_blueprint(api)

if __name__ == '__main__':
    app.run(debug=True, port=8080)

from init import app, db
from flask import Blueprint, render_template, request
from models import *

api = Blueprint('api', __name__, template_folder='api_responses', url_prefix='/api')

@app.route("/")
def hello_world():
    return render_template('home.html')

@api.route('/test', methods=["POST"])
def test():
    sample = request.form['sample']
    db.session.add(Test(sample=sample))
    db.session.commit()
    return render_template('test.html', value=sample)

app.register_blueprint(api)

if __name__ == '__main__':
    app.run(debug=True)

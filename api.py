from init import db
from models import *
from flask import Blueprint, redirect, request, render_template, url_for

api = Blueprint('api', __name__, template_folder='api_responses', url_prefix='/api')

@api.route('/test', methods=["POST"])
def test():
    sample = request.form['sample']
    db.session.add(Test(sample=sample))
    db.session.commit()
    return render_template('test.html', value=sample)

@api.route('/redirect', methods=["POST"])
def redirect_route():
    return redirect(url_for('another'))

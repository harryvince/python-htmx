from init import db
from models import *
from flask import Blueprint, redirect, request, render_template, url_for, jsonify

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

@api.route('/json', methods=["GET"])
def return_json():
    query = db.session.query(AnotherTest.id, AnotherTest.name, Test.sample).join(Test)
    value = query.all()
    if value == None:
        return jsonify({})
    return f"{query}; {value}"

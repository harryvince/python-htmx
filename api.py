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
    query = db.session.query(*AnotherTest.__table__.columns, *Test.__table__.columns).filter(AnotherTest.test_id == Test.id)
    value = query.all()
    if value == None:
        return jsonify({})
    return f"{query}; {value}"

@api.route('/select', methods=["GET"])
def return_select():
    id = request.args.get("id")
    if id == None:
        return jsonify({ 'error': 'no id provided' })
    tests = db.session.query(Test).all()
    return render_template('select.html', tests=tests, id=int(id))

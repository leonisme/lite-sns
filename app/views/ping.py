from ..app import app
from flask import jsonify


@app.route('/ping')
def ping():
    return jsonify(pong=True)
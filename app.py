from flask import Flask, jsonify, request
from flask_cors import CORS
from werkzeug import exceptions
from flask_sqlalchemy import SQLAlchemy
from os import path
# from . import URL

app = Flask(__name__)
CORS(app)

db = SQLAlchemy()
DB_NAME = 'database.db'

app.config['SECRET_KEY'] = "helloworld"
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return jsonify({'message': 'Hello from Flask!'}), 200


@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return {'message': f'Oops! {err}'}, 404


@app.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return {'message': f'Oops! {err}'}, 400


@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return {'message': f"It's not you, it's us"}, 500


if __name__ == "__main__":
    app.run(debug=True)

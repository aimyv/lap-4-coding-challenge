from flask import Flask, jsonify, request
from flask_cors import CORS
from werkzeug import exceptions
from flask_sqlalchemy import SQLAlchemy
from os import path

import math
import random


app = Flask(__name__)
CORS(app)

db = SQLAlchemy()
DB_NAME = 'database.db'

app.config['SECRET_KEY'] = "helloworld"
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
db.init_app(app)


class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    long_path = db.Column(db.Text, nullable=False, unique=True)
    short_path = db.Column(db.String(50), unique=True)


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return jsonify({'message': 'Hello from Flask!'}), 200


@app.route('/urls', methods=['GET', 'POST'])
def urls_handler():
    if request.method == 'GET':
        urls = Url.query.all()
        outputs = map(lambda p: {
                      "id": p.id, "long_path": p.long_path, "short_path": p.short_path}, urls)
        usableOutputs = list(outputs)
        return jsonify(usableOutputs), 200
    elif request.method == 'POST':
        uData = request.json
        foundUrl = Url.query.filter_by(long_path=uData["long_path"]).first()
        if foundUrl:
            output = {"id": foundUrl.id, "long_path": foundUrl.long_path,
                      "short_path": foundUrl.short_path}
            return output, 200
        else:
            count = Url.query.count()
            code = 'https://ap/' + getrandom()
            new_url = Url(
                id=count+1, long_path=uData["long_path"], short_path=code)
            db.session.add(new_url)
            db.session.commit()
            output = {"id": new_url.id, "long_path": new_url.long_path,
                      "short_path": new_url.short_path}
            return jsonify(output), 201


def getrandom():
    text = ''
    possible = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    for i in range(5):
        text += possible[random.randint(0, len(possible)-1)]
    return text


@app.route('/urls/<int:url_id>', methods=['GET', 'DELETE'])
def specific_urls_handler(url_id):
    if request.method == 'GET':
        try:
            foundUrl = Url.query.filter_by(id=url_id).first()
            output = {"id": foundUrl.id, "long_path": foundUrl.long_path,
                      "short_path": foundUrl.short_path}
            return output
        except:
            raise exceptions.BadRequest(
                f"We do not have a url with that id: {url_id}")
    elif request.method == 'DELETE':
        try:
            foundUrl = Url.query.filter_by(id=url_id).first()
            db.session.delete(foundUrl)
            db.session.commit()
            return "deleted", 204
        except:
            raise exceptions.BadRequest(
                f"failed to delete a url with that id: {url_id}")


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

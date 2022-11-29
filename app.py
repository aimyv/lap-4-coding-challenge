from flask import Flask, jsonify, request
from flask_cors import CORS
from werkzeug import exceptions
from flask_sqlalchemy import SQLAlchemy
from os import path


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
        new_url = Url(
            id=uData["id"], long_path=uData["long_path"], short_path=uData["short_path"])
        db.session.add(new_url)
        db.session.commit()
        return jsonify(uData), 201


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

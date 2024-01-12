from flask import Flask, request
from flask_restx import Resource, Api

app = Flask(__name__)
api = Api(app)

VERIFY_TOKEN = "Hello"


@api.route('/webhook')
class HelloWorld(Resource):
    def get(self):

        return {'hello': 'world'}


if __name__ == '__main__':
    app.run(debug=True)

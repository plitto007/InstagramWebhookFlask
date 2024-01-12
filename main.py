from flask import Flask, request
from flask_restx import Resource, Api

app = Flask(__name__)
api = Api(app)

VERIFY_TOKEN = "Hello"


@api.route('/webhook')
class HelloWorld(Resource):
    def get(self):
        challenge = request.args.get("hub.challenge")
        verify_token = request.args.get("hub.verify_token")
        if verify_token == VERIFY_TOKEN:
            return challenge, 200
        return "", 400


if __name__ == '__main__':
    app.run(debug=True)

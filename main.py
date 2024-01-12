from flask import Flask, request
from flask_restx import Resource, Api

app = Flask(__name__)
api = Api(app)

VERIFY_TOKEN = "Hello"


@api.route('/webhook')
class HelloWorld(Resource):
    def get(self):
        mode = request.args.get("hub.mode")
        challenge = request.args.get("hub.challenge")
        verify_token = request.args.get("hub.verify_token")
        if mode == "subscribe" and verify_token == VERIFY_TOKEN:
            return int(challenge), 200

        return "", 200

    def post(self):
        body = request.get_json(force=True)
        print("Body webhook: {}".format(body))
        return 200


if __name__ == '__main__':
    app.run(debug=True)

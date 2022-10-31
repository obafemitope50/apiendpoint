from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/')
def index():
    """ Render a JSON response. """
    return jsonify(
        slackUsername="Lego",
        backend=True,
        age=22,
        bio="Just another regular guy.")

if __name__ == '__main__':
    app.run()

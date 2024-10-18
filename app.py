from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return "<h1>Welcome to my Flask app!</h1>"


@app.route('/greet', methods=['GET'])
def greet():
    name = request.args.get('name')
    return f"<h2>Hello {name}</h2>"


if __name__ == '__main__':
    app.run(debug=True)

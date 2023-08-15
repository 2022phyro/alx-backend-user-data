from flask import Flask, jsonify, abort, request
from flask_cors import CORS, cross_origin
from auth import Auth


AUTH = Auth()
app = Flask(__name__)
@app.route("/", methods=['GET'])
def greet():
    """Gives a greeting"""
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=['POST'], strict_slashes=False)
def signin():
    em = request.form.get('email')
    pwd = request.form.get('password')
    try:
        user = AUTH.register_user(em, pwd)
        return jsonify({"email": em, "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400
if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)

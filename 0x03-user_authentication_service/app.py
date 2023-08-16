#!/usr/bin/env python3
"""A minimalist app"""
from flask import Flask, jsonify, abort, request, redirect, url_for
from auth import Auth

AUTH = Auth()
app = Flask(__name__)


@app.route("/", methods=['GET'])
def greet():
    """Gives a greeting"""
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=['POST'], strict_slashes=False)
def signup():
    """Signs up a user"""
    em = request.form.get('email')
    pwd = request.form.get('password')
    try:
        user = AUTH.register_user(em, pwd)
        return jsonify({"email": em, "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=['POST'], strict_slashes=False)
def login():
    """"Logs in a user"""
    em = request.form.get('email')
    pwd = request.form.get('password')
    valid = AUTH.valid_login(em, pwd)
    if not valid:
        abort(401)
    s_id = AUTH.create_session(em)
    res = jsonify({'email': em, 'message': 'logged in'})
    res.set_cookie('session_id', s_id)
    return res


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """Logs out a user"""
    s_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(s_id)
    if not user:
        abort(403)
    AUTH.destroy_session(user.id)
    return redirect('/')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

#!/usr/bin/env python3
"""A minimalist app"""
from flask import Flask, jsonify, abort, request

app = Flask(__name__)


@app.route("/", methods=['GET'])
def greet():
    """Gives a greeting"""
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)

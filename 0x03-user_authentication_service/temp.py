

class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """Initializes the db"""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Tries to register a user"""
        try:
            user = self._db.find_user_by(email=email)
            raise ValueError(f'User {email} already exists')
        except (NoResultFound, InvalidRequestError):
            pwd = _hash_password(password)
            return self._db.add_user(email, pwd)

    def valid_login(self, email: str, password: str,) -> bool:
        """Validates a login
        Args:
            email (str): the user email
            password (str): the user password
        Returns:
            bool: if the passwords are a match or not
        """
        try:
            user = self._db.find_user_by(email=email)
            pwd = password.encode()
            return bcrypt.checkpw(pwd, user.hashed_password)
        except (NoResultFound, InvalidRequestError):
            return False

    def _generate_uuid(self) -> str:
        """Returns a new UUID"""
        return str(uuid.uuid4())


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

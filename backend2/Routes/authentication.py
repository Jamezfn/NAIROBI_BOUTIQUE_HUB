from flask import Blueprint, request


auth = Blueprint('authentication', __name__)

@auth.route('/register', methods=['POST'])
def register():
    """
    Register a new user.
    Expects JSON data with 'username', 'password', and 'role'.
    """
    from Controllers.user_controller import register_user
    username = request.form["username"],
    email = request.form["email"],
    password = request.form["password"]
    role = request.form["role"]

    return register_user(username, email, password, role)

@auth.route('/login', methods=['POST'])
def login():
    """
    Log in a user.
    Expects JSON data with 'username' and 'password'.
    """
    from Controllers.user_controller import login_user
    email = request.form["email"]
    password = request.form["password"]
    return login_user(email, password)

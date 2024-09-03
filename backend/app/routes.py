from flask import Blueprint, request, jsonify
from app import db
from app.models import User, Shop, Product, BucketList
from app.auth import validate_token

bp = Blueprint('api', __name__)

@bp.route('/register', methods=['POST'])
def register():
    """
    Register a new user.
    Expects JSON data with 'username', 'password', and 'role'.
    """
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    role = data.get('role')

    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'User already exists'}), 400

    new_user = User(username=username,
            password_hash=bcrypt.generate_password_hash(password).decode('utf-8'),
            role=role)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201

@bp.route('/login', methods=['POST'])
def login():
    """
    Log in a user.
    Expects JSON data with 'username' and 'password'.
    """
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()

    if user and bcrypt.check_password_hash(user.password_has, password):
        access_token = create_access_token(identity=user.user.id)
        return jsonify({'access_token': access_token}), 200

    return jsonify({'message': 'Invalid credentials'}), 401

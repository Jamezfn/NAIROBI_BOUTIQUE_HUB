from database.db import db
from flask import jsonify
from Models.user_model import User
from utils.password_manager import encrypt_password, check_password


def  register_user(username, email, password, role):
    """saves user to the database"""
    if username is None: return jsonify({'error': 'Missing username'}), 400
    if email is None: return jsonify({'error': 'Missing email'}), 400
    if password is None: return jsonify({'error': 'Missing password'}), 400
    if role is None: return jsonify({'error': 'Missing role'}), 400
    

    if User.query.filter_by(username=username).first():
        return jsonify({'error': 'User with username already existrs'}), 400

    encrypted_password = encrypt_password(password)
    
    new_user = User(username=username, email=email, password_hash=encrypted_password, role=role)

    db.session.commit()
    db.session.add(new_user)

    return ({'user': {'username': new_user.username, 'email': new_user.email, 'role': new_user.role}}), 200


def login_user(email, password):
    """login user"""
    if email is None: return jsonify({'error': 'Missing email'}), 400
    if password is None: return jsonify({'error': 'Missing password'}), 400

    user = User.query.filter_by(email=email).first()
    if not user: return jsonify({'error': 'user does not exist'}), 400

    if not check_password(password, user.password_hash):
        return jsonify({'error': 'Incorrect password'})
    return jsonify({'message': 'Login successful', 'user': {
        'username': user.username,
        'email': user.email,
        'role': user.role
    }}), 200
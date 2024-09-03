import os
import jwt
from functools import wraps
from flask import request, jsonify

SECRET_KEY = os.getenv('SECRET_KEY', 'kista_amezutd')

def generate_token(user_id):
    """
    Generate a JWT token.
    """
    try:
        payload = {'user_id': user_id}
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        return token
    except Exception as e:
        print(f"Error generating token: {e}")
        return None

def validate_token(token):
    """
    Validate JWT token.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        print("Token has expired.")
        return None
    except jwt.InvalidTokenError:
        print("Invalid token.")
        return None

def token_required(f):
    """
    Decorator to check for a valid token in the request.
    """
    @wraps(f)
    def decorated_function(*args , **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].replace('Bearer ', "")
        if not token:
            return jsonify({'message': 'Token is missing!'}), 403

        payload = validate_token(token)
        if not payload:
            return jsonify({'message': 'Invalid or expired token!'}), 403
        return f(*args, **kwargs)
    return decorated_function

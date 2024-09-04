import bcrypt


def encrypt_password(plain_password):
    """encrypts a password"""
    bytes = plain_password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(bytes, salt)

    return hash


def check_password(plain_password, hash):
    """checks if user has entered the correct password"""
    bytes = plain_password.encode('utf-8')
    return bcrypt.checkpw(bytes, hash)
#!/usr/bin/env python3

from flask import Flask
from database.db import db




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///project.db"

db.init_app(app)

from Routes.authentication import auth
app.register_blueprint(auth, url_prefix='/auth')
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
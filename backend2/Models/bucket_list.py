from app import db
from datetime import datetime


class BucketList(db.Model):
    """
    Represents a user's bucket list item
    which tracks products a user wants.
    """
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('product.id'),nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    added_on = db.Column(db.DateTime, default=datetime.utcnow)
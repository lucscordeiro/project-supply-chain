from app import db
from datetime import datetime

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.String(100), unique=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    origin = db.Column(db.String(255), nullable=False)
    transactions = db.relationship('Transaction', backref='product', lazy=True)

    def __repr__(self):
        return f'<Product {self.product_id} - {self.name}>'

class Transaction(db.Model):
    __tablename__ = 'transactions'
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.String(100), db.ForeignKey('products.product_id'), nullable=False)
    from_entity = db.Column(db.String(255), nullable=False)
    to_entity = db.Column(db.String(255), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return f'<Transaction {self.id} - {self.product_id}>'

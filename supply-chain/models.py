from database import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    supplier = db.Column(db.String(100))
    location = db.Column(db.String(100))

class Stage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    date_time = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(100))
    responsible = db.Column(db.String(100))
    additional_info = db.Column(db.String(200))
    product = db.relationship('Product', backref=db.backref('stages', lazy=True))

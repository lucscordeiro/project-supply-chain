from flask import request, jsonify
from models import Product, Stage
from database import db

def register_routes(app):
    @app.route('/products', methods=['POST'])
    def add_product():
        data = request.json
        product = Product(
            name=data['name'],
            description=data.get('description'),
            supplier=data.get('supplier'),
            location=data.get('location')
        )
        db.session.add(product)
        db.session.commit()
        return jsonify({'message': 'Product added'}), 201

    @app.route('/stages', methods=['POST'])
    def add_stage():
        data = request.json
        stage = Stage(
            product_id=data['product_id'],
            date_time=data['date_time'],
            location=data['location'],
            responsible=data.get('responsible'),
            additional_info=data.get('additional_info')
        )
        db.session.add(stage)
        db.session.commit()
        return jsonify({'message': 'Stage added'}), 201

    @app.route('/products/<int:product_id>', methods=['GET'])
    def get_product(product_id):
        product = Product.query.get_or_404(product_id)
        stages = Stage.query.filter_by(product_id=product_id).all()
        return jsonify({
            'product': {
                'id': product.id,
                'name': product.name,
                'description': product.description,
                'supplier': product.supplier,
                'location': product.location
            },
            'stages': [{'date_time': stage.date_time, 'location': stage.location, 'responsible': stage.responsible, 'additional_info': stage.additional_info} for stage in stages]
        })

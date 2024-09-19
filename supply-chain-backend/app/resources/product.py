from flask_restful import Resource, reqparse
from flask import current_app
from flask import jsonify

parser = reqparse.RequestParser()
parser.add_argument('product_id', type=str, required=True, help='Product ID is required')
parser.add_argument('name', type=str, required=True, help='Product name is required')
parser.add_argument('origin', type=str, required=True, help='Product origin is required')

class ProductResource(Resource):
    def get(self, product_id):
        manager = current_app.supply_chain_manager
        product = manager.get_product(product_id)
        if not product:
            return {'message': 'Product not found'}, 404
        return {
            'product_id': product.product_id,
            'name': product.name,
            'origin': product.origin,
            'transactions': [t.id for t in product.transactions],
            'merkle_root': manager.get_merkle_root()
        }, 200

class ProductListResource(Resource):
    def get(self):
        manager = current_app.supply_chain_manager
        products = manager.product_table.keys()
        sorted_products = list(products)
        from app.utils.algorithms import merge_sort
        merge_sort(sorted_products)
        return {'products': sorted_products}, 200

    def post(self):
        manager = current_app.supply_chain_manager
        args = parser.parse_args()
        try:
            product = manager.add_product(
                product_id=args['product_id'],
                name=args['name'],
                origin=args['origin']
            )
            return {
                'message': 'Product created successfully',
                'product': {
                    'product_id': product.product_id,
                    'name': product.name,
                    'origin': product.origin
                }
            }, 201
        except ValueError as ve:
            return {'message': str(ve)}, 400

from flask_restful import Resource, reqparse
from flask import current_app
from flask import jsonify
from app.models import Transaction  # Importação necessária

parser = reqparse.RequestParser()
parser.add_argument('product_id', type=str, required=True, help='Product ID is required')
parser.add_argument('from_entity', type=str, required=True, help='From entity is required')
parser.add_argument('to_entity', type=str, required=True, help='To entity is required')

class TransactionResource(Resource):
    def get(self, transaction_id):
        manager = current_app.supply_chain_manager
        transaction = Transaction.query.get(transaction_id)
        if not transaction:
            return {'message': 'Transaction not found'}, 404
        return {
            'id': transaction.id,
            'product_id': transaction.product_id,
            'from_entity': transaction.from_entity,
            'to_entity': transaction.to_entity,
            'timestamp': transaction.timestamp.isoformat()
        }, 200

class TransactionListResource(Resource):
    def get(self):
        manager = current_app.supply_chain_manager
        transactions = Transaction.query.all()
        result = []
        for t in transactions:
            result.append({
                'id': t.id,
                'product_id': t.product_id,
                'from_entity': t.from_entity,
                'to_entity': t.to_entity,
                'timestamp': t.timestamp.isoformat()
            })
        return {'transactions': result}, 200

    def post(self):
        manager = current_app.supply_chain_manager
        args = parser.parse_args()
        try:
            transaction = manager.add_transaction(
                product_id=args['product_id'],
                from_entity=args['from_entity'],
                to_entity=args['to_entity']
            )
            return {
                'message': 'Transaction added successfully',
                'transaction': {
                    'id': transaction.id,
                    'product_id': transaction.product_id,
                    'from_entity': transaction.from_entity,
                    'to_entity': transaction.to_entity,
                    'timestamp': transaction.timestamp.isoformat()
                },
                'merkle_root': manager.get_merkle_root()
            }, 201
        except ValueError as ve:
            return {'message': str(ve)}, 400

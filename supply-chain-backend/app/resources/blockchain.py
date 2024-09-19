from flask_restful import Resource
from flask import current_app
from flask import jsonify

class BlockchainResource(Resource):
    def get(self):
        """
        Retorna toda a cadeia de blocos.
        """
        manager = current_app.supply_chain_manager
        chain = manager.get_blockchain()
        response = {
            'length': len(chain),
            'chain': chain
        }
        return response, 200

    def post(self):
        """
        Inicia a mineração das transações pendentes.
        """
        manager = current_app.supply_chain_manager
        mined_index = manager.mine_transactions()
        if not mined_index:
            return {'message': 'No transactions to mine'}, 400
        return {'message': 'Block mined', 'block_index': mined_index}, 201

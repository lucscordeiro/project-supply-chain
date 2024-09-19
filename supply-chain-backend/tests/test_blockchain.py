import unittest
from app import create_app, db
from app.models import Product, Transaction
from app.utils.supply_chain_manager import SupplyChainManager

class BlockchainTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()
            self.manager = SupplyChainManager()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_blockchain_creation(self):
        with self.app.app_context():
            chain = self.manager.get_blockchain()
            self.assertEqual(len(chain), 1)  # Apenas o bloco gênesis

    def test_add_transaction_and_mine(self):
        with self.app.app_context():
            # Adicionar produto
            self.manager.add_product('P001', 'Produto Teste', 'Origem Teste')
            # Adicionar transação
            self.manager.add_transaction('P001', 'Fornecedor A', 'Distribuidor B')
            # Minear transações
            mined_index = self.manager.mine_transactions()
            self.assertEqual(mined_index, 1)
            # Verificar cadeia de blocos
            chain = self.manager.get_blockchain()
            self.assertEqual(len(chain), 2)
            self.assertEqual(chain[1]['index'], 1)
            self.assertEqual(len(chain[1]['transactions']), 1)
            self.assertEqual(chain[1]['transactions'][0]['product_id'], 'P001')

    def test_no_transactions_to_mine(self):
        with self.app.app_context():
            response = self.client.post('/api/blockchain')
            self.assertEqual(response.status_code, 400)
            self.assertIn('No transactions to mine', response.get_json()['message'])

if __name__ == '__main__':
    unittest.main()

import unittest
from app import create_app, db
from app.models import Product, Transaction
from app.utils.supply_chain_manager import SupplyChainManager

class TransactionTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()
            self.manager = SupplyChainManager()
            self.manager.add_product('P001', 'Produto Teste', 'Origem Teste')

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_add_transaction(self):
        with self.app.app_context():
            transaction = self.manager.add_transaction('P001', 'Fornecedor A', 'Distribuidor B')
            self.assertIsNotNone(transaction)
            self.assertEqual(transaction.product_id, 'P001')
            self.assertEqual(transaction.from_entity, 'Fornecedor A')
            self.assertEqual(transaction.to_entity, 'Distribuidor B')

    def test_get_transaction_history(self):
        with self.app.app_context():
            self.manager.add_transaction('P001', 'Fornecedor A', 'Distribuidor B')
            self.manager.add_transaction('P001', 'Distribuidor B', 'Varejista C')
            history = self.manager.get_transaction_history('P001')
            self.assertEqual(len(history), 2)

    def test_add_transaction_nonexistent_product(self):
        with self.app.app_context():
            with self.assertRaises(ValueError):
                self.manager.add_transaction('P999', 'Fornecedor A', 'Distribuidor B')

if __name__ == '__main__':
    unittest.main()

import unittest
from app import create_app, db
from app.models import Product
from app.utils.supply_chain_manager import SupplyChainManager

class ProductTestCase(unittest.TestCase):
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

    def test_add_product(self):
        with self.app.app_context():
            product = self.manager.add_product('P001', 'Produto Teste', 'Origem Teste')
            self.assertIsNotNone(product)
            self.assertEqual(product.product_id, 'P001')

    def test_get_product(self):
        with self.app.app_context():
            self.manager.add_product('P001', 'Produto Teste', 'Origem Teste')
            product = self.manager.get_product('P001')
            self.assertIsNotNone(product)
            self.assertEqual(product.name, 'Produto Teste')

    def test_duplicate_product(self):
        with self.app.app_context():
            self.manager.add_product('P001', 'Produto Teste', 'Origem Teste')
            with self.assertRaises(ValueError):
                self.manager.add_product('P001', 'Produto Duplicado', 'Outra Origem')

if __name__ == '__main__':
    unittest.main()

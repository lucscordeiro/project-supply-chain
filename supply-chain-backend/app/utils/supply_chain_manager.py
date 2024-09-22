from .data_structures import LinkedList, Graph, HashTable
from flask_sqlalchemy import SQLAlchemy
from app.models import Product, Transaction
from .merkle_tree import MerkleTree
from .blockchain import Blockchain
from app import db


# db = SQLAlchemy()

class SupplyChainManager:
    def __init__(self):
        self.transaction_history = LinkedList()
        self.graph = Graph()
        self.product_table = HashTable()
        self.merkle_tree = MerkleTree()
        self.blockchain = Blockchain()

    def load_data(self):
        """Carregar produtos e transações no contexto da aplicação."""
        self._load_products()
        self._load_transactions()

    def _load_products(self):
        products = Product.query.all()
        for product in products:
            self.product_table.insert(product.product_id, product)

    def _load_transactions(self):
        transactions = Transaction.query.order_by(Transaction.timestamp).all()
        for transaction in transactions:
            self.transaction_history.append(transaction.id)
            self.graph.add_edge(transaction.from_entity, transaction.to_entity)
            self.merkle_tree.update_tree(str(transaction.id))
            txn_data = {
                'transaction_id': transaction.id,
                'product_id': transaction.product_id,
                'from_entity': transaction.from_entity,
                'to_entity': transaction.to_entity,
                'timestamp': transaction.timestamp.isoformat()
            }
            self.blockchain.add_new_transaction(txn_data)

    def add_product(self, product_id, name, origin):
        if self.product_table.search(product_id):
            raise ValueError("Product ID already exists.")
        new_product = Product(product_id=product_id, name=name, origin=origin)
        db.session.add(new_product)
        db.session.commit()
        self.product_table.insert(product_id, new_product)
        return new_product

    def get_product(self, product_id):
        return self.product_table.search(product_id)

    def add_transaction(self, product_id, from_entity, to_entity):
        product = self.get_product(product_id)
        if not product:
            raise ValueError("Product not found.")

        new_transaction = Transaction(
            product_id=product_id,
            from_entity=from_entity,
            to_entity=to_entity
        )
        db.session.add(new_transaction)
        db.session.commit()

        self.transaction_history.append(new_transaction.id)
        self.graph.add_edge(from_entity, to_entity)
        self.merkle_tree.update_tree(str(new_transaction.id))

        txn_data = {
            'transaction_id': new_transaction.id,
            'product_id': new_transaction.product_id,
            'from_entity': new_transaction.from_entity,
            'to_entity': new_transaction.to_entity,
            'timestamp': new_transaction.timestamp.isoformat()
        }
        self.blockchain.add_new_transaction(txn_data)

        return new_transaction

    def get_transaction_history(self, product_id):
        product = self.get_product(product_id)
        if not product:
            raise ValueError("Product not found.")

        transactions = Transaction.query.filter_by(product_id=product_id).order_by(Transaction.timestamp).all()
        history = [t.id for t in transactions]
        return history

    def get_supply_chain_path(self, from_entity, to_entity):
        return self.graph.find_path(from_entity, to_entity)

    def get_merkle_root(self):
        return self.merkle_tree.get_root()

    def mine_transactions(self):
        mined_index = self.blockchain.mine()
        return mined_index

    def get_blockchain(self):
        chain_data = []
        for block in self.blockchain.chain:
            chain_data.append({
                'index': block.index,
                'timestamp': block.timestamp,
                'transactions': block.transactions,
                'nonce': block.nonce,
                'hash': block.hash,
                'previous_hash': block.previous_hash
            })
        return chain_data

    def get_sorted_product_ids(self):
        product_ids = self.product_table.keys()
        sorted_ids = list(product_ids)
        from .algorithms import merge_sort
        merge_sort(sorted_ids)
        return sorted_ids

    def search_product_binary(self, product_id):
        sorted_ids = self.get_sorted_product_ids()
        from .algorithms import binary_search
        index = binary_search(sorted_ids, product_id)
        if index != -1:
            return self.product_table.search(sorted_ids[index])
        return None

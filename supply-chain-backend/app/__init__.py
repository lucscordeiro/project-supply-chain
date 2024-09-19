from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_restful import Api

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)
    api = Api(app)

    with app.app_context():
        from app.utils.supply_chain_manager import SupplyChainManager
        from app.models import Product, Transaction  # Importa os modelos
        
        db.create_all()  # Cria as tabelas se ainda não existirem
        
        supply_chain_manager = SupplyChainManager()
        app.supply_chain_manager = supply_chain_manager
        supply_chain_manager.load_data()  # Carrega produtos e transações

        from app.resources.product import ProductResource, ProductListResource
        from app.resources.transaction import TransactionResource, TransactionListResource
        from app.resources.blockchain import BlockchainResource

        api.add_resource(ProductListResource, '/api/products')
        api.add_resource(ProductResource, '/api/products/<string:product_id>')
        api.add_resource(TransactionListResource, '/api/transactions')
        api.add_resource(TransactionResource, '/api/transactions/<int:transaction_id>')
        api.add_resource(BlockchainResource, '/api/blockchain')

    return app

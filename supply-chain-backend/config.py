import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Configuração do SQLAlchemy
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Configurações adicionais podem ser adicionadas aqui

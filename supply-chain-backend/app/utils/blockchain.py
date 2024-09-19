import hashlib
import json
from time import time

class Block:
    def __init__(self, index, timestamp, transactions, previous_hash, nonce=0):
        self.index = index
        self.timestamp = timestamp
        self.transactions = transactions  # Lista de transações
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.compute_hash()

    def compute_hash(self):
        """
        Calcula o hash do bloco atual.
        """
        block_string = json.dumps(self.__dict__, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

class Blockchain:
    difficulty = 2  # Número de zeros à esquerda do hash

    def __init__(self):
        self.unconfirmed_transactions = []  # Transações pendentes
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        """
        Cria o bloco gênesis e adiciona à cadeia.
        """
        genesis_block = Block(0, time(), [], "0")
        genesis_block.hash = genesis_block.compute_hash()
        self.chain.append(genesis_block)

    @property
    def last_block(self):
        return self.chain[-1]

    def proof_of_work(self, block):
        """
        Implementa o algoritmo de prova de trabalho.
        """
        block.nonce = 0
        computed_hash = block.compute_hash()
        while not computed_hash.startswith('0' * Blockchain.difficulty):
            block.nonce += 1
            computed_hash = block.compute_hash()
        return computed_hash

    def add_block(self, block, proof):
        """
        Adiciona um bloco à cadeia após validação.
        """
        previous_hash = self.last_block.hash
        if previous_hash != block.previous_hash:
            return False

        if not self.is_valid_proof(block, proof):
            return False

        block.hash = proof
        self.chain.append(block)
        return True

    def is_valid_proof(self, block, block_hash):
        """
        Verifica se o hash é válido.
        """
        return (block_hash.startswith('0' * Blockchain.difficulty) and
                block_hash == block.compute_hash())

    def add_new_transaction(self, transaction):
        print(f"Adding transaction: {transaction}")
        self.unconfirmed_transactions.append(transaction)

    def mine(self):
        """
        Minerar as transações pendentes.
        """
        if not self.unconfirmed_transactions:
            print("No transactions to mine.")
            return False

        last_block = self.last_block

        new_block = Block(index=last_block.index + 1,
                          timestamp=time(),
                          transactions=self.unconfirmed_transactions,
                          previous_hash=last_block.hash)

        print(f"Mining block: {new_block.__dict__}")

        proof = self.proof_of_work(new_block)

        if self.add_block(new_block, proof):
            print(f"Block mined and added: {new_block.__dict__}")
            self.unconfirmed_transactions = []
            return new_block.index
        else:
            print("Failed to add block.")
            return False

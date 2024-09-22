import hashlib

class MerkleTree:
    def __init__(self, leaves=None):
        self.leaves = leaves if leaves else []
        self.root = self.build_merkle_tree(self.leaves)

    def hash_data(self, data):
        return hashlib.sha256(data.encode('utf-8')).hexdigest()

    def build_merkle_tree(self, nodes):
        if not nodes:
            return None
        if len(nodes) == 1:
            return nodes[0]
        new_level = []
        for i in range(0, len(nodes), 2):
            left = nodes[i]
            right = nodes[i + 1] if i + 1 < len(nodes) else left
            new_hash = self.hash_data(left + right)
            new_level.append(new_hash)
        return self.build_merkle_tree(new_level)

    def update_tree(self, new_leaf):
        self.leaves.append(new_leaf)
        self.root = self.build_merkle_tree(self.leaves)

    def get_root(self):
        return self.root

    def verify_integrity(self, data, proof):
        pass

import hashlib

def hash_data(data):
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

def create_merkle_tree(leaves):
    if len(leaves) % 2 != 0:
        leaves.append(leaves[-1])
    tree = [leaves]
    while len(tree[-1]) > 1:
        level = []
        for i in range(0, len(tree[-1]), 2):
            combined = tree[-1][i] + tree[-1][i + 1]
            level.append(hash_data(combined))
        tree.append(level)
    return tree

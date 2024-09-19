# Lista Ligada
class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = ListNode(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def find(self, key):
        current = self.head
        while current and current.data != key:
            current = current.next
        return current

    def to_list(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

# Pilha
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

# Fila
from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()

    def is_empty(self):
        return len(self.queue) == 0

    def peek(self):
        if not self.is_empty():
            return self.queue[0]

# Árvore Binária (para demonstração; não diretamente utilizada no grafo)
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Grafo usando listas de adjacência
class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, from_vertex, to_vertex):
        self.add_vertex(from_vertex)
        self.add_vertex(to_vertex)
        self.adj_list[from_vertex].append(to_vertex)

    def get_neighbors(self, vertex):
        return self.adj_list.get(vertex, [])

    def to_dict(self):
        return self.adj_list

# Tabela Hash
class HashTable:
    def __init__(self, size=100):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def search(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def delete(self, key):
        index = self._hash(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return True
        return False

    def keys(self):
        keys = []
        for bucket in self.table:
            for pair in bucket:
                keys.append(pair[0])
        return keys

    def values(self):
        values = []
        for bucket in self.table:
            for pair in bucket:
                values.append(pair[1])
        return values

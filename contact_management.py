# class for the binary tree node
class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None
        
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, key, data):
        new_node = Node(key, data)
        if not self.root:
            self.root = new_node
        else: 
            self._insert_recursive(self.root, new_node)
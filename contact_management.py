# class for the binary tree node
class Node:
    def __init__(self, key, data):
        self.key = key  # name
        self.data = data    # phone number / email
        self.left = None
        self.right = None
        
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    # create a new node at the root if one does exist already
    def insert(self, key, data):
        new_node = Node(key, data)
        if not self.root:
            self.root = new_node
        else: 
            self._insert_recursive(self.root, new_node)
            
    def _insert_recursive(self, current, new_node):
        # 
        if new_node.key < current.key:
            if current.left is None:
                current.left = new_node
            else:
                self._insert_recursive(current.left, new_node)
        elif new_node.key > current.key:
            if current.right is None:
                current.right = new_node
            else:
                self._insert_recursive(current.right, new_node)
                
    def search(self, key):
        return self._search_recursive(self.root, key)
    
    def _search_recursive(self, current, key):
        if not current:
            return None
        if key == current.key:
            return current.data
        elif key < current.key:
            return self._search_recursive(current.left, key)
        else: 
            return self._search_recursive(current.right, key)
        
    def display(self):
        self._display_recursive(self.root)
        
    def _display_recursive(self, current, depth=0):
        if current:
            self._display_recursive(current.left, depth + 1)
            print(" " * depth * 2, current.key, "->", current.data)
            self._display_recursive(current.right, depth + 1)

# Test Implementation
contacts = BinarySearchTree()
contacts.insert("Alice", "alice@example.com")
contacts.insert("Bob", "bob@example.com")
contacts.insert("Charlie", "charlie@example.com")
contacts.insert("Jeffrey", "jeffrey@example.com")

print("Contact Search: ", contacts.search("Bob"))
print("All Contacts:")
contacts.display()
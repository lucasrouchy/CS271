# HashTable: An unordered key-value data structure providing O(1) store, retrieve
# search and delete operations.
# Your implementation should pass the tests in test_hash_table.py.
# YOUR NAME


class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.data = [[] for i in range(size)]
    
        
        
        

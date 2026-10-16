class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, key):
        return sum(ord(char) for char in key)

    def add(self, key, value):
        hash_value = self.hash(key)
        if hash_value not in self.collection:
            self.collection[hash_value] = {}
        self.collection[hash_value][key] = value

    def remove(self, key):
        hash_value = self.hash(key)
        # Check if the hash_value exists and the key is in the nested dictionary
        if hash_value in self.collection and key in self.collection[hash_value]:
            del self.collection[hash_value][key]
            # Clean up the empty dictionary if no keys are left at this hash value
            if not self.collection[hash_value]:
                del self.collection[hash_value]

    def lookup(self, key):
        hash_value = self.hash(key)
        # Return the value if the key exists, otherwise return None
        if hash_value in self.collection and key in self.collection[hash_value]:
            return self.collection[hash_value][key]
        return None

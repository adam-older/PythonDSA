class HashTable:
    def __init__(self):
        self.INITIAL_CAPACITY = 50
        self.capacity = self.INITIAL_CAPACITY
        self.size = 0
        self.buckets = [None] * self.capacity

    class Node:
        def __init__(self, key, value) -> None:
            self.key = key
            self.value = value
            self.next = None
    
    def hash(self, key):
        hashsum = 0
        # for each character in the key
        for idx, c in enumerate(key):
            # add (index + length of key) ^ (current char code)

            hashsum += (idx + len(key)) ** ord(c)
            # perform modulus to keep hashsum in range [0, self.capacity - 1]

            hashsum = hashsum % self.capacity
        return hashsum

    def insert(self, key, value):
        # 1. increment size
        self.size += 1
        # 2. compute index of key using hash function
        hashedindex = self.hash(key)

        # 3. if bucket at index is empty, create new node and add it there
        node = self.buckets[hashedindex]
        newNode = self.Node(key, value)
        if node is None:
            self.buckets[hashedindex] = newNode
            return
        # 4. if bucket is not empty, iterate to end of list and add node there
        else:
            prev = node
            while node is not None:
                node = node.next
            prev.next = node

    def find(self, key):
        # 1. compute index using hash function
        index = self.hash(key)
        # 2. go to bucket for index
        node = self.buckets[index]
        # 3. iterate thru nodes, until key is found or end of list is reached
        while node is not None and node.key != key:
            node = node.next
        # 4. return found node or None
        if node is None:
            return None
        else:
            return node.value


ht = HashTable()
ht.insert("hello", "world")
ht.insert("test", "testing")

print(ht.find("hello"))
print(ht.find("hellos"))
print(ht.find("test"))


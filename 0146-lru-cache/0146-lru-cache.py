class Node:
    """
    Doubly-linked-list node used by LRUCache.
    Stores (key, value) so we can delete the key from the hashmap when evicting.
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None



class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> Node

        # Dummy head and tail to avoid edge cases
        self.head = Node(0, 0)  # Most recently used
        self.tail = Node(0, 0)  # Least recently used

        self.head.next = self.tail
        self.tail.prev = self.head


        
    # Remove a node from the linked list
    def _remove(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    # Insert node right after head (MRU position)
    def _insert(self, node):
        first = self.head.next

        self.head.next = node
        node.prev = self.head

        node.next = first
        first.prev = node
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # Move accessed node to front (MRU)
        self._remove(node)
        self._insert(node)

        return node.value
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update existing node
            node = self.cache[key]
            node.value = value

            # Move to front
            self._remove(node)
            self._insert(node)
        else:
            # If capacity exceeded, remove LRU
            if len(self.cache) == self.capacity:
                lru = self.tail.prev
                self._remove(lru)
                del self.cache[lru.key]

            # Insert new node
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._insert(new_node)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
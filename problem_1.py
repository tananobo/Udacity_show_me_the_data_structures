class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        if capacity < 1:
            print("capacity should more than 1, then set capacity = 1")
            capacity = 1
        self.capacity = int(capacity)
        # self.num_elements = 0
        self.head = None
        self.tail = None
        self.cache = {}

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key in self.cache:
            node = self.cache[key]
            self._move_to_front(node)
            print("get:", node.value)
            return node.value
        print("-1 : this key is not in the cache")
        return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_front(node)
            return

        node = Node(key, value)

        if len(self.cache) == self.capacity:
            del self.cache[self.tail.key]
            self._remove_node(self.tail)

        self.cache[key] = node
        self._add_first(node)
    
    def _move_to_front(self, node):
        self._remove_node(node)
        self._add_first(node)

    def _remove_node(self, node):
        prev_node = node.prev
        next_node = node.next

        if prev_node:
            prev_node.next = next_node
        else:
            self.head = next_node

        if next_node:
            next_node.prev = prev_node
        else:
            self.tail = prev_node
    
    def _add_first(self, node):
        node.next = self.head
        node.prev = None

        if self.head:
            self.head.prev = node

        self.head = node

        if self.tail == None:
            self.tail = node

    


# TEST 1
print("======TEST1======: Udacity provides")
our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(9)      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

# TEST 2
print("======TEST2======: shortest cache")
our_cache = LRU_Cache(1)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


our_cache.get(1)       # returns -1
our_cache.get(4)       # returns 4
our_cache.get(9)      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) # returns -1
our_cache.set(6, 6) # returns -1

our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

print("======TEST3======: Capacity is less than 1")
our_cache = LRU_Cache(-1.5)

print("======TEST4======")
our_cache = LRU_Cache(3.5) 
our_cache.set(1, 1)
our_cache.set(2, "Noboru")
our_cache.set(3, 3)
our_cache.set(4, 4)


our_cache.get(1)       # returns 1
our_cache.get(2)       # returns "Noboru"
our_cache.get(9)      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
import sys
from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        # Max number of nodes it can hold
        self.limit = limit
        # Current number of nodes it is holding
        self.size = 0
        self.order = DoublyLinkedList()
        self.storage = dict()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.storage:
            print(f'yes, I did find {key} here')
            node = self.storage[key]
            print(self.order)
            self.order.move_to_front(node)
            print(self.order)
            print(f'then returning \'{node.value[1]}\'')
            return node.value[1]
        else:
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        if key in self.storage:
            node = self.storage[key]
            node.value = (key, value)
            self.order.move_to_front(node)
            return
        print(f'this is the size: {self.size}')
        print(f'this is the limit: {self.limit}')
        if self.size == self.limit:
            print(self.storage)
            print(f'wil remove {self.order.tail.value}')
            print(f'the head {self.order.head.value}')
            print(self.order)
            print("value bracket", self.order.tail.value[0])
            del self.storage[self.order.tail.value[0]]
            print(self.storage)
            name = self.order.remove_from_tail()
            print('name', name)
            print('removed', self.order)
            self.size -= 1
        
        self.order.add_to_head((key, value))
        self.storage[key] = self.order.head
        self.size += 1


# lruTest = LRUCache(3)
# lruTest.set("item1", "a")
# lruTest.set("item2", "b")
# lruTest.set("item3", "c")
# lruTest.get("item1")
# lruTest.set("item4", "d")

# print(lruTest.get("a"))

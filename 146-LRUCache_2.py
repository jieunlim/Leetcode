#Could you do both operations in O(1) time complexity?

# Ordered dictionary
# Python - OrderedDict
# Java - LinkedHashMap
# time - O(1), space - O(capacity)
# 1) get(key) - return value /-1 if not exists in the
# cache
# 2) put(key, value) - set or insert/ invalidate LRU
# item if the cache reached it’s capacity 

from collections import OrderedDict
class LRUCache(OrderedDict):

    def __init__(self, capacity: int):
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self: return -1
        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        self[key] = value
        
        if len(self) > self.capacity:
            self.popitem(last =False)

            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

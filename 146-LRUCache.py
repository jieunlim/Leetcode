class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
        

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {} #key : Node
        self.head = Node()
        self.tail = Node()
        
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, key: int) -> int:
        #if exist: remove, move to back
        if key in self.dic:
            node = self.dic[key]
            self.remove(node)
            self.add(node)
            
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        #exist: remove, update dic, add back to the linkedlist
        
        if key in self.dic:
            node = self.dic[key]
            self.remove(node)
        self.dic[key] = Node(key, value)
        self.add(self.dic[key])
        
        #if full: remove old node : head.next, remove dic
        if len(self.dic) > self.capacity:
            node = self.head.next
            self.remove(node)
            del self.dic[node.key]
            
    
    def add(self, node):
        #add to the end
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
        
         
        
    def remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p
        
# Solution2, add and remove function using key instead of node
        
class Node:
    
    def __init__(self, key=0, val=0):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        
        self.head = Node
        self.tail = Node
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        if key in self.dic:
            node = self.dic[key]
            self.remove(key)
            self.add(key)
            return self.dic[key].val
        return -1
        
        
    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            node = self.dic[key]
            self.remove(key)
        self.dic[key] = Node(key, value)
        self.add(key)
        
        if len(self.dic) > self.capacity:
            node = self.head.next
            self.remove(node.key)
            del self.dic[node.key]
            
        
    def remove(self, key):
        node = self.dic[key] 

        p = node.prev
        n = node.next

        p.next = n
        n.prev = p


        
    def add(self, key):
        node = self.dic[key] 
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node
        
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

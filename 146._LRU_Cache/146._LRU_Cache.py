class Node:
        def __init__(self, key, value):
            self.value = value
            self.key = key
            self.prev = None
            self.next = None
class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert(self, node):
        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
        self.tail = node
    def delete(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
            
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dli = DLL()
        self.cache_dict = {}
        
    def get(self, key: int) -> int:
        if key in self.cache_dict:
            value = self.cache_dict[key].value
            self.dli.delete(self.cache_dict[key])
            node = Node(key, value)
            self.dli.insert(node)
            self.cache_dict[key] = node
            return value
        return (-1)        

    def put(self, key: int, value: int) -> None:
        if key in self.cache_dict:
            self.dli.delete(self.cache_dict[key])
        elif len(self.cache_dict) >= self.capacity:
            del self.cache_dict[self.dli.head.key]
            self.dli.delete(self.dli.head)
        node = Node(key, value)
        self.dli.insert(node)
        self.cache_dict[key] = node
      
    
      
            
            
            
        
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

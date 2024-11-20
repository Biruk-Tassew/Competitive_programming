class Node:
    def __init__(self, value=-1, key=-1, next_node = None, prev_node = None):
        self.value = value
        self.key = key
        self.next_node = next_node
        self.prev_node = prev_node
        
class LRUCache:
    def __init__(self, capacity: int):
        self.head = Node()
        self.tail = Node(-1, -1, None, self.head)
        self.head.next_node = self.tail
        self.key_value = {}
        self.capacity = capacity

    def make_recently_used(self, node: Node) -> None:
        # cut the node out of where it's
        node.prev_node.next_node = node.next_node
        node.next_node.prev_node = node.prev_node

        # put it after the head
        node.next_node = self.head.next_node
        self.head.next_node.prev_node = node
        self.head.next_node = node
        node.prev_node = self.head

    def get(self, key: int) -> int:
        if key in self.key_value:
            node = self.key_value[key]
            self.make_recently_used(node)
            return self.key_value[key].value

        return -1

    def put(self, key: int, value: int) -> None:

        if key in self.key_value:
            self.key_value[key].value = value
            self.make_recently_used(self.key_value[key])
        else:
            if len(self.key_value) >= self.capacity:
                lru_node = self.tail.prev_node

                # remove the lru node from the dictionary and the linkedlist
                self.key_value.pop(lru_node.key)
                lru_node.prev_node.next_node = self.tail
                self.tail.prev_node = lru_node.prev_node 

            new_node = Node(value, key, self.head.next_node, self.head)
            self.head.next_node = new_node
            new_node.next_node.prev_node = new_node
            self.key_value[key] = new_node

        
    
 
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
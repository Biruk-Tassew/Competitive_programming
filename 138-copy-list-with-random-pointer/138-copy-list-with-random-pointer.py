"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        new_nodes = {None:None}
        
        temp = head
        while temp:
            new_nodes[temp] = Node(temp.val)
            temp = temp.next
        
        temp = head
        while temp:
            new_nodes[temp].next = new_nodes[temp.next]
            new_nodes[temp].random = new_nodes[temp.random]
            temp = temp.next
            
        return new_nodes[head]
        
        
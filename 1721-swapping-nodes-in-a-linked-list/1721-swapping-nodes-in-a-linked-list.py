# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        first_node = None
        second_node = None
        temp = head
        
        while temp:
            
            k -= 1
            second_node = None if not second_node else second_node.next
            
            if not k:
                first_node = temp
                second_node = head
            temp = temp.next
            
            
        first_node.val, second_node.val = second_node.val, first_node.val
        return head
            
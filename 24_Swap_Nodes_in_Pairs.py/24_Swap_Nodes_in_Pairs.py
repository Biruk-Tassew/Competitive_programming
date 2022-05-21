# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        comp = ListNode(0)
        comp.next = head
        cur = comp
    
        while cur.next and cur.next.next:
            left = cur.next
            right = cur.next.next
            
            left.next = right.next
            cur.next = right
            right.next = left
            
            cur = left
            
        return comp.next

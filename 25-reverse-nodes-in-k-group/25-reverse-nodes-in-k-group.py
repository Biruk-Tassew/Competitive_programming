# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        node_count = k
        while node_count:
            if not cur:
                return head
            
            cur = cur.next
            node_count -= 1
            
        n_head = self.reverse(head, cur)
        head.next = self.reverseKGroup(cur, k)
        return n_head
    def reverse(self, head, tail):
        prev = None
        cur = head
        
        while cur != tail:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
            
        return prev
    
    
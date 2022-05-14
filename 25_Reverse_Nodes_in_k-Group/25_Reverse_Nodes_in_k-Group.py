# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head, tail):
        prev = None
        cur = head
        temp = None
        
        while cur != tail:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
            
        return prev
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        
        count = k
        comp = head
        
        while count > 0:
            if not comp:
                return head
            comp = comp.next
            count -= 1
        tail = comp
        count = k
        
        nHead = self.reverseList(head, tail)
        head.next = self.reverseKGroup(tail, k)
        
        return nHead
            
        

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        comp = head
        while head.next:
            count += 1
            head = head.next
            
        if count%2 == 0:
            count = count/2
            while count > 0 and comp.next:
                comp = comp.next
                count -= 1
            return comp
        
        count = count//2
        count += 1
        while count > 0 and comp.next:
            comp = comp.next
            count -= 1
        return comp
        
                
            
        

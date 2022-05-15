# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:        
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        comp = ListNode(float('-inf'))
        
        while head:
            prev = comp

            while prev:
                
                if head.val >= prev.val and (not prev.next or head.val <= prev.next.val):
                    
                    temp = head.next
                    head.next = prev.next
                    prev.next = head
                    head = temp
                    break
                prev = prev.next
                
        return comp.next
            
            
        

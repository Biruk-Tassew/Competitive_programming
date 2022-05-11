# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    
        passDig = 0
        temp = None
        store = None
        
        while l1 or l2:
            cSum = passDig
            if l1:
                cSum += l1.val
                l1 = l1.next
            if l2:
                cSum += l2.val
                l2 = l2.next
                
            node = ListNode(cSum % 10)
            passDig = cSum//10
            
            if not temp:
                temp = store = node
            else:
                temp.next = node
                temp = temp.next
                
        if passDig > 0:
            temp.next = ListNode(passDig)
            
        return store
            
            
            
        
        
            
                
            
        
            
                    
                
            

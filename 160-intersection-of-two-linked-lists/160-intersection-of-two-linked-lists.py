# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        pathOne = headA
        pathTwo = headB
        
        while pathOne != pathTwo:
            if pathOne:
                pathOne = pathOne.next
            else:
                pathOne = headB
                
            if pathTwo:
                pathTwo = pathTwo.next
            else:
                pathTwo = headA
                
        return pathOne